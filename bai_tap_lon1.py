def Nhap_tu(s):
    while True:
        try:
            tu = input('Nhập %s' % s)
            if all(item == ' ' or item.isalpha() for item in tu):
                return tu
            else:
                print('Đây không phải là từ. Yêu cầu nhập lại')
        except Exception as err:
            print(err)


def Nhapso():
    while True:
        try:
            n = int(input('Chọn chức năng cần thực hiện (1-6): '))
        except ValueError:
            print('Đây không phải là số nguyên. Yêu cầu nhập lại')
        else:
            if 1 <= n <= 6:
                return n
            else:
                print('Đây không phải là số nguyên từ 1 đến 6. Yêu cầu nhập lại')


def them_tu(dic):
    print('\t1.- Thêm từ')
    word = Nhap_tu('từ mới: ')

    # Tìm vị trí để chèn từ mới theo thứ tự tăng dần
    for i, (w, _) in enumerate(dic):
        if w == word:
            print("Từ này đã tồn tại trong từ điển.")
            return
        elif w > word:
            pos = i
            break
    else:
        pos = len(dic)

    meanings = []
    while True:
        print("Nhập thông tin cho nghĩa thứ", len(meanings) + 1)
        part_of_speech = input("Loại từ (danh từ, động từ, tính từ, ...): ")
        meaning = Nhap_tu("nghĩa: ")
        example = Nhap_tu("ví dụ: ")
        meanings.append((part_of_speech, meaning, example))

        more_meanings = input("Thêm nghĩa khác cho từ này? (yes/no): ")
        if more_meanings.lower() != 'yes':
            break

    dic.insert(pos, (word, meanings))
    print('Từ mới đã được thêm vào từ điển.')


def Tim_tu(dic):
    print('\t2.- Tìm từ')
    word = Nhap_tu('từ cần tìm: ')
    for w, meanings in dic:
        if w == word:
            print('Tìm thấy từ %s trong từ điển:' % word)
            for idx, (part_of_speech, meaning, example) in enumerate(meanings, 1):
                print(f"Nghĩa thứ {idx}:")
                print(f"Loại từ: {part_of_speech}")
                print(f"Nghĩa: {meaning}")
                print(f"Ví dụ: {example}")
            return
    print('Không tìm thấy từ %s trong từ điển' % word)


def xoa_tu(dic):
    print('\t3.- Xóa từ:')
    word = Nhap_tu('từ cần xóa: ')
    for i, (w, _) in enumerate(dic):
        if w == word:
            print('Từ cần xóa: [%s : %s]' % (word, dic[i]))
            dic.pop(i)
            print('Từ đã được xóa.')
            return
    print('Không tìm thấy từ %s cần xóa' % word)


def luu_vao_tep(dic, filename):
    with open(filename, 'w') as f:
        for word, meanings in dic:
            f.write(word + ':')
            for meaning in meanings:
                f.write(','.join(meaning) + ';')
            f.write('\n')
    print(f"Từ điển đã được lưu vào file {filename}")


def nap_tu_tep(filename):
    dic = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            parts = line.strip().split(':')
            word = parts[0]
            meanings = [tuple(part.split(',')) for part in parts[1].split(';') if part]
            dic.append((word, meanings))
    dic.sort(key=lambda x: x[0])  # Sắp xếp lại mảng theo thứ tự từ
    return dic


def menu():
    print('\n=====CHƯƠNG TRÌNH TẠO TỪ ĐIỂN=====')
    print('\t1.- Thêm từ')
    print('\t2.- Tìm từ')
    print('\t3.- Xóa từ')
    print('\t4.- Lưu từ điển vào file')
    print('\t5.- Nạp từ điển từ file')
    print('\t6.- Kết thúc chương trình')


def main():
    dic = []
    while True:
        menu()
        choice = Nhapso()
        if choice == 6:
            print('Chương trình tạo từ điển kết thúc')
            break
        elif choice == 1:
            them_tu(dic)
        elif choice == 2:
            Tim_tu(dic)
        elif choice == 3:
            xoa_tu(dic)
        elif choice == 4:
            filename = input("Nhập tên tập tin để lưu từ điển: ")
            luu_vao_tep(dic, filename)
        elif choice == 5:
            filename = input("Nhập tên tập tin để nạp từ điển: ")
            dic = nap_tu_tep(filename)
            print(f"Từ điển đã được nạp từ file {filename}")
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

main()
