class RestaurantBill:
    def __init__(self, id, customer_name, table_number, food_amount, vat_rate, service_fee, discount):
        self.id = id
        self.customer_name = customer_name
        self.table_number = table_number
        self.food_amount = food_amount
        self.vat_rate = vat_rate
        self.service_fee = service_fee
        self.discount = discount
        self.total_bill = 0
        self.bill_type = ""

        def calculate_total_bill(self):
            money_vat = food_amount * vat_rate / 100
            total_bill = food_amount + money_vat + service_fee - discount
        
        def classify_bill(self):
            if self.total_bill < 500_000:
                self.bill_type = "Nhỏ"
            elif self.total_bill < 2_000_000:
                self.bill_type = "Trung Bình"
            elif self.total_bill < 5_000_000:
                self.bill_type = "Lớn"
            else:
                self.bill_type = "VIP"

class RestaurantBillManager:
    def __init__(self):
        self.bills = []

    def add_bill(self):
        while True:
            bill_id = input("Nhập vào mã hóa đơn: ")
            for bill in self.bills:
                if bill_id.lower() == bill.id.lower():
                    print("Mã đơn không được trùng, Vui lòng nhập lại")
                    return
            if not bill_id:
                print("Mã đơn không được để trống")
                return
            
            else:
                customer_name = input("Nhập vào tên khách hàng: ")
                if not customer_name:
                    print("tên khách hàng không được trống")
                    return

                table_number = input("Nhập vào số bàn: ")
                if not table_number:
                    print("Số bàn không được rỗng")
                    return

                food_amount = int(input("Nhập số tiền món ăn: "))
                if food_amount < 0:
                    print("Số tiền món ăn phải lớn hơn hoặc bằng 0")
                    return

                vat_rate = float(input("Nhập tỉ lệ VAT: "))
                if vat_rate < 0 or vat_rate > 100:
                    print("tỉ lệ vat phải từ 0 - 100")
                    return

                service_fee = int(input("Nhập phí dịch vụ: "))
                if service_fee < 0:
                    print("Phí dịch vụ phải lớn hơn hoặc bằng 0")
                    return

                discount = float(input("Giảm giá: "))
                if discount < 0:
                    print("giảm giá phải lớn hơn hoặc bằng 0")
                    return

                
                bill = RestaurantBill(id, customer_name, table_number, food_amount, vat_rate, service_fee, discount)
                # bill.calculate_total_bill()
                # bill.classify_bill()
                self.bills.append(bill)
                print("Đã thêm thành công")
                return


    def show_all(self):
        if not self.bills:
            print("Danh sách hóa đơn bàn ăn đang rỗng")
            return
        
        print(f"{'Mã hóa đơn':<5} | {'Tên khách hàng':<20} | {'Số bàn':<2} | {'Tiền món ăn':<9} | {'Tỷ lệ VAT':<4} | {'Phí dịch vụ':<9} | {'Giảm giá':<5} | {'Tổng tiền hóa đơn':<9} | {'Phân loại hóa đơn':<10}")
        for bill in self.bills:
            print(f"{bill.id:<5} | {bill.customer_name:<20} | {bill.table_number:<2} | {bill.food_amount:<9} | {bill.vat_rate:<4} | {bill.service_fee:<9} | {bill.discount:<5} | {bill.total_bill:<9} | {bill.bill_type:<10}")
        
    def delete_bill(self):
        if not self.bills:
            print("Danh sách hóa đơn bàn ăn đang rỗng")
            return
        
        bill_id = input("Nhập vào mã hóa đơn cần xóa: ")
        if not bill_id:
            print("Dữ liệu không được trống")
            return
        for bill in self.bills:
            if bill_id.lower() == bill.id.lower():
                self.bills.remove(bill)
        else:
            print("Không tìm thấy mã đơn món")

    def search_bill(self):
        if not self.bills:
            print("Danh sách hóa đơn bàn ăn đang rỗng")
            return
        bill_id = input("nhập mã hóa đơn cần tìm: ")
        result = []
        if not bill_id:
            print("Dữ liệu không được trống")
            return

        for bill in self.bills:
            if bill_id.lower() == bill.id.lower():
                print("Đã tìm thấy đơn món")
                self.bills.append(result)
                break
        else:
            print("Không tìm thấy mã đơn món")

        print(result)


def main():
    restaurant_Bill = RestaurantBillManager()
    while True:
        header = f" MENU ".center(50, "=")
        user_choice = input(f"""
{header}
1. Hiển thị danh sách hóa đơn bàn ăn 
2. Thêm hóa đơn
3. Cập nhật hóa đơn
4. Xóa hóa đơn
5. Tìm kiếm hóa đơn 
6. Thoát
{'='*len(header)}
Nhập lựa chọn của bạn (1-6): """)
        match user_choice:
            case "1":
                restaurant_Bill.show_all()
            case "2":
                restaurant_Bill.add_bill()
            case "3":
                pass
            case "4":
                restaurant_Bill.delete_bill()
            case "5":
                restaurant_Bill.search_bill()
            case "6":
                print("Thoát chương trình.....")
                break
            case _:
                print("lựa chọn không hợp lệ, vui lòng nhập lại")
if __name__ == "__main__":
    main()