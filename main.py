from os import scandir


def read_file(path):
    file = open(path, 'r')
    text = file.read()
    file.close()
    return text


def clean(s):
    return s.replace(" ", "").replace("\t", "").replace("\n", "")


def calculate_similarity(s1, s2, difference):
    return round((1 - (difference / max(len(s1), len(s2)))) * 100, 2)


def levenshtein_distance(s1, s2):
    m, n = len(s1) + 1, len(s2) + 1
    d = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        d[i][0] = i
    for j in range(n):
        d[0][j] = j

    for j in range(1, n):
        for i in range(1, m):
            if s1[i - 1] == s2[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                d[i][j] = min(d[i][j - 1], d[i - 1][j], d[i - 1][j - 1]) + 1
    return d[len(s1)][len(s2)]


def equal(s1, s2):
    return s1 == s2


def read_folder_meta(path):
    return filter(lambda x: x.name.endswith('.java') or x.name.endswith('.c') or x.name.endswith('.py'), scandir(path))


if __name__ == '__main__':
    base_path = input("Enter a folder:")
    print(f"==========================Folder: {base_path}==========================")
    for entry0 in read_folder_meta(base_path):
        content0 = read_file(entry0.path)
        print(f"- {entry0.name}")
        for entry1 in read_folder_meta(base_path):
            if entry1.name == entry0.name:
                continue
            content1 = read_file(entry1.path)

            diff_with_tap_n_space, diff = levenshtein_distance(content0, content1), \
                                          levenshtein_distance(clean(content0), clean(content1))

            probability_with_tap_n_space, probability = calculate_similarity(content0, content1, diff_with_tap_n_space), \
                                                        calculate_similarity(clean(content0), clean(content1), diff)

            print(f"\t|_____{entry1.name}")
            print(f"\t\t|_____there are {probability}% of plagiarism without taps and spaces")
            print(f"\t\t|_____there are {probability_with_tap_n_space}% of plagiarism with taps and spaces")
            if equal(clean(content0), clean(content1)):
                print(f"\t\t|_____files are equal")
            if probability > 70 and probability_with_tap_n_space > 30:
                print(f"\t\t|_____is possible that the user try to hide plagiarism with taps and spaces")
