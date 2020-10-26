
import pytest
import time
from data.class_party.class_party_privateinformation_data import ClassParty_Send_PrivateInformation_Data
class Test_ClassParty_PrivateInformation():

    @pytest.mark.parametrize("cases",ClassParty_Send_PrivateInformation_Data)
    def test_send_private_information(self,cases,ClassParty_PrivateInformation):
        privateinformatin_page = ClassParty_PrivateInformation

        # 点击联系人
        privateinformatin_page.PrivateInformation_Click_Contacts()
        #选择py31
        privateinformatin_page.PrivateInformation_Click_Py31_Class()
        #选择联系人
        privateinformatin_page.PrivateInformation_Click_Choice_Contacts()
        #点击文本框
        privateinformatin_page.PrivateInformation_Click_Message_Input()
        #输入私信内容
        privateinformatin_page.PrivateInformation_Input_Chat_Text(cases["message"])
        #点击发送
        privateinformatin_page.PrivateInformation_Click_Send_Out()
