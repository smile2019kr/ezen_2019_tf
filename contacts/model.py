from contacts.contact import Contact
class ContactsModel:
    def __init__(self):
        pass

#정보 입력
    @staticmethod
    def set_contact(name, tel, email, address):
        contact = Contact(name, tel, email, address)
        return contact
    # 1명의 개인정보를 상정 (contact 단수)

    def print_info(self):
        str = '이름: {} \n 전화번호: {} \n 이메일: {} \n 주소: {}'\
               .format(self.name, self.tel, self.email, self.address)
        return str

#정보 가져오는 것
    @staticmethod
    def get_contacts(params):
        contacts = []
        for i in params:
            contacts.append(i.to_string())
        return ''.join(contacts)
    # 여러명의 개인정보를 가져오는 것을 상정

#정보 삭제
    @staticmethod
    def del_contact(params, name):
        for i, t in enumerate(params):
            if t.name == name:
                del params[i]
