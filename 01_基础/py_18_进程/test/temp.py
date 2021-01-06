for i in range(100):
    file_name = "temp_" + str(i) + ".txt"
    file = open(file_name, '+w')
    file.write(str(i) * 100)
    file.close()
