class Contact:
    def __init__(self, name, tel, email, address):
        self.name = name
        self.tel = tel
        self.email = email
        self.address = address

    def to_string(self):
        t = '이름: {} \n 전화번호: {} \n 이메일: {} \n 주소: {}\n'\
                .format(self.name, self.tel, self.email, self.address)
        return t