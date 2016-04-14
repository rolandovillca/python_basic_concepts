try:
    f = open('test.txt', encoding='utf-8')
    # hereperform file operations
finally:
    f.close()