
def read_line(path):
    # Insert code here
    return None


def read_file(path):
    # Insert code here
    return None


def compare(file_path1, file_path2):
    similarity_indicator = 100
    # Insert code here
    # Use levenshtein per line
    # When you have all lines compare calculate the similarity per file
    return similarity_indicator


def read_folder_meta_data_file(path):
    list_of_files_names = []
    # Insert code here
    return list_of_files_names


def print_similarity_report(**kwargs):
    print("""
    Folder: path
        - Student 1 (filename) 
            |_____ It's 100% similar to Student 2 (filename)
            |_____ It's 100% similar to Student 3 (filename)
        - Student 2 (filename) 
            |_____ It's 100% similar to Student 1 (filename)
            |_____ It's 100% similar to Student 3 (filename)
        - Student 3 (filename) 
            |_____ It's 100% similar to Student 2 (filename)
            |_____ It's 100% similar to Student 1 (filename)                                             
    
    """)


if __name__ == '__main__':
    print("main")
