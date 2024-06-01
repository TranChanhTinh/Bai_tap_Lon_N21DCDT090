mang_muc_tu = []# Tạo một mảng lưu trữ các mục từ

def them_muc_tu(tu, loai_tu, nghia, vi_du):
    for item in mang_muc_tu:
        if item[0] == tu:
            item.append((loai_tu, nghia, vi_du))
            print(f"Đã thêm nghĩa mới cho từ '{tu}'.")
            return
    mang_muc_tu.append([tu, (loai_tu, nghia, vi_du)])
    print(f"Đã thêm từ '{tu}' vào từ điển với nghĩa: '{nghia}'.")

def loai_bo_muc_tu(tu):
    for item in mang_muc_tu:
        if item[0] == tu:
            mang_muc_tu.remove(item)
            print(f"Đã loại bỏ từ '{tu}' khỏi từ điển.")
            return
    print(f"Từ '{tu}' không tồn tại trong từ điển.")

def tra_cuu_nghia(tu):
    for item in mang_muc_tu:
        if item[0] == tu:
            print(f"Nghĩa của từ '{tu}':")
            for nghia in item[1:]:
                print(f"  Loại từ: {nghia[0]}")
                print(f"  Nghĩa: {nghia[1]}")
                print(f"  Ví dụ: {nghia[2]}")
            return
    print(f"Từ '{tu}' không tồn tại trong từ điển.")

def luu_tu_dien(ten_tap_tin):
    try:
        with open(ten_tap_tin, 'w') as file:
            for item in mang_muc_tu:
                file.write(f"{item[0]}\n")
                for nghia in item[1:]:
                    file.write(f"  {nghia[0]} | {nghia[1]} | {nghia[2]}\n")
        print(f"Từ điển đã được lưu vào tập tin '{ten_tap_tin}'.")
    except Exception as e:
        print(f"Lỗi khi lưu từ điển vào tập tin '{ten_tap_tin}': {e}")

def nap_tu_dien(ten_tap_tin):
    try:
        global mang_muc_tu
        mang_muc_tu = []
        with open(ten_tap_tin, 'r') as file:
            lines = file.readlines()
            tu_hien_tai = None
            nghia = []
            for line in lines:
                if not line.startswith("  "):
                    if tu_hien_tai:
                        mang_muc_tu.append([tu_hien_tai] + nghia)
                    tu_hien_tai = line.strip()
                    nghia = []
                else:
                    loai_tu, nghia_text, vi_du = line.strip().split(" | ")
                    nghia.append((loai_tu, nghia_text, vi_du))
            if tu_hien_tai:
                mang_muc_tu.append([tu_hien_tai] + nghia)
        print(f"Từ điển đã được nạp từ tập tin '{ten_tap_tin}'.")
    except FileNotFoundError:
        print(f"Tập tin '{ten_tap_tin}' không tồn tại.")
    except Exception as e:
        print(f"Lỗi khi nạp từ điển từ tập tin '{ten_tap_tin}': {e}")

print("\nChào mừng bạn đến với Từ điển Anh-Anh!")
while True:
    print("Hãy chọn một trong các tùy chọn sau:")
    print("1. Thêm một mục từ mới")
    print("2. Loại bỏ một mục từ")
    print("3. Tra cứu nghĩa của một mục từ")
    print("4. Lưu từ điển vào tập tin")
    print("5. Nạp từ điển từ tập tin")
    print("6. Thoát")
    lua_chon = input("Nhập lựa chọn của bạn : ")

    if lua_chon == '1':
        tu_moi = input("Nhập từ mới: ")
        loai_tu_moi = input("Nhập loại từ: ")
        nghia_moi = input("Nhập nghĩa của từ: ")
        vi_du_moi = input("Nhập ví dụ: ")
        them_muc_tu(tu_moi, loai_tu_moi, nghia_moi, vi_du_moi)
    elif lua_chon == '2':
        tu_can_loai_bo = input("Nhập từ cần loại bỏ: ")
        loai_bo_muc_tu(tu_can_loai_bo)
    elif lua_chon == '3':
        tu_can_tra_cuu = input("Nhập từ cần tra cứu: ")
        tra_cuu_nghia(tu_can_tra_cuu)
    elif lua_chon == '4':
        ten_tap_tin = input("Nhập tên tập tin để lưu từ điển: ")
        luu_tu_dien(ten_tap_tin)
    elif lua_chon == '5':
        ten_tap_tin = input("Nhập tên tập tin để nạp từ điển: ")
        nap_tu_dien(ten_tap_tin)
    elif lua_chon == '6':
        print("Cảm ơn bạn đã sử dụng Từ điển Anh-Anh. Tạm biệt!")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
