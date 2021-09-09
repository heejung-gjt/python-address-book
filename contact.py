class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def print_info(self):
        print('이름 : {} , 전화번호 : {} , 이메일 : {} , 주소 : {}'.format(self.name, self.phone, self.email, self.address))


def set_contact():
    name = input('name :')
    phone = input('phone :')
    email = input('email :')
    address = input('address :')
    contact = Contact(name, phone, email, address)
    return contact


def print_menu():
    print('1. 연락처 입력')
    print('2. 연락처 출력')
    print('3. 연락처 삭제')
    print('4. 종료')
    menu = int(input('메뉴선택 :'))
    return menu


def print_contact(lists):
    for list in lists: # contact객체
        list.print_info() # 객체에대한 infor를 출력


def delete_contact(lists, name):
    for i, contact in enumerate(lists):
        if contact.name == name:
            del lists[i]


def store_contact(lists):
    f = open('contact_list_db.txt', 'wt', encoding='CP949')
    for list in lists:
        f.write(list.name + '\n')
        f.write(list.phone + '\n')
        f.write(list.email + '\n')
        f.write(list.address + '\n')
    f.close()


def load_contact(lists):
    f = open('contact_list_db.txt', 'rt', encoding='CP949')
    lines = f.readlines()
    num = len(lines) / 4
    num = int(num)
    for i in range(num):
        name = lines[4 * i].rstrip('\n')
        phone = lines[4 * i + 1].rstrip('\n')
        email = lines[4 * i + 2].rstrip('\n')
        address = lines[4 * i + 3].rstrip('\n')
        contact = Contact(name, phone, email, address)
        lists.append(contact)
    f.close()


def run():
    contact_list = []
    load_contact(contact_list)
    while True:
        menu = print_menu()
        if menu == 1:
            contact = set_contact()
            contact_list.append(contact)
        if menu == 2:
            print_contact(contact_list)
        if menu == 3:
            name = input('주소록을 삭제하실 이름을 입력하세요: ')
            delete_contact(contact_list, name)
        if menu == 4:
            store_contact(contact_list)
            break
        
   
if __name__ == "__main__":
    run()