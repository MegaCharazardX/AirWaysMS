import re

reg_ex = re.compile(r"^\b[a-zA-Z0-9]+@[a-z]+.[a-z]\b")
class _gmail_:
    def __init__(self, _match, _gmail = None):
        self.__gmail = _gmail
        self.__match = _match
        
    def _isVlaid(self):
        if self.__match is None:
            return "Invalid Email Address"
        return "Valid Email Address" #'<Match: %r, groups=%r>' % (match.group(), match.groups())


gmail = _gmail_(input("Enter Gmail Address : "))
print(gmail._isVlaid(reg_ex.match(gmail)))