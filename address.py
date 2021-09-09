# -*- coding: EUC-KR -*-
class Contact:
  def __init__(self, name, phone_number, e_mail, addr):
    self.name = name
    self.phone_number = phone_number
    self.e_mail = e_mail
    self.addr = addr

  def __repr__(self):
    print('name', self.name)

  def print_info(self):
    print('name',self.name)


def set_contact():
  name = input('name:')
  phone_number = input('phone_number:')
  e_email = 


def run():
  kim = Contact('손희정', '010-222-222', 'dkfkfkf@naver.com', 'seoul')
  kim.print_info()

if __name__=="__main__":
  run()
