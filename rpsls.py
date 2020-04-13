#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ���̩Դ
���ڣ�2020/4/13
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
	"""
	����Ϸ�����Ӧ����ͬ������
	"""

    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��
	if name=='ʯͷ':
		return 0
	elif name=='ʷ����':
		return 1
	elif name=='ֽ':
		return 2
	elif name=='����':
		return 3
	elif name=='����':
		return 4
	else:
		print('Error:No Correct Name')




def number_to_name(number):
	"""
	������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
	"""   
	if number==0:# ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
		return 'ʯͷ'
	elif number==1:
		return 'ʷ����'
	elif number==2:
		return 'ֽ'
	elif number==3:
		return '����'
	else:
		return '����'# ��Ҫ���Ƿ��ؽ��
   




def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """


    print("-------- ")# ���"-------- "���зָ�
    print('����ѡ��Ϊ:',player_choice)# ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice
    
    player_choice_number=name_to_number(player_choice)# ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number
    import random as ra
    comp_number=ra.randint(0,4)# ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    comp_choice=number_to_name(comp_number)# ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    print('�������ѡ��Ϊ��',comp_choice)# ����Ļ����ʾ�����ѡ����������

    if player_choice_number-comp_number==1 or player_choice_number-comp_number==2: # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��
        print('��Ӯ��')
    elif player_choice_number-comp_number==0: # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�
        print("���ͼ������һ����")	
    else:
        print("�����Ӯ��")
   




# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)


