import re
from decorator_params import logger

@logger('main2.log')
def clear_phone_format(phone):
  regex = r"(\+7|8)?\s*\(?(\d{1,3})\)?[-\s]*(\d{1,3})[-\s]*(\d{1,2})[-\s]*(\d{1,2})\s*\(?(доб.)?\s*(\d+)?\)?"
  clear_phone_with_adds = r"+7(\2)\3-\4-\5 \6\7"
  clear_phone_wo_adds = r"+7(\2)\3-\4-\5"

  if "доб." in phone:
    return re.sub(regex, clear_phone_with_adds, phone)
  else: 
    return re.sub(regex, clear_phone_wo_adds, phone)
  

if __name__ == '__main__':
    target_phone = '+7(906)-198-7643'

    clear_phone_format(target_phone)