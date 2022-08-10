# Data-processing-tool-by-lzg
有问题请联系:ahu_ai@163.com

people的文件架构应该为
peopleTest
  |--P_test_teach1
    |--Series-017
    |--Series-026
  |--P_test_teach2
  |--P_test_teach3
  
  1 运行rename.py 对文件目录进行重命名
  peopleTest
  |--P_test_teach1
    |--CT
    |--PET
  函数内参数 dir_name = 'peopleTest' //peopleTest改成自己保存命名的目录名
  
  2 运行CT image removal check bed algorithm3.py 对CT图像进行脑部检查床去除
  函数内参数 ROOT_DIR = 'peopleTest' //peopleTest改成自己保存命名的目录名
  
  3 运行Data Enhancement.py 进行数据的旋转扩增
  参数   ROOT_DIR = 'peopleTest' //peopleTest改成自己保存命名的目录名
        a, b, c = -45, 50, 3  //a,b为旋转的角度间隔,左闭又开,c为间隔,如 从-45每隔3度进行旋转保存,直到旋转为45度结束
  
  4 运行train_init.py 
  参数 ROOT_DIR = "peopleTest"  //peopleTest改成自己保存命名的目录名
      TRAIN_DIR = 'train_init_test' //保存的文件名称
  对上述处理数据进行初始化,最终生成一份基于 peopleTest 文件目录下所有人的CT-PET对应数据集
  数据架构为
  train_init_test
    |--CT
    |--PET
  其中,CT-PET为一一对应图
  
  5 运行image_merge.py 对PC-PET进行合成并列的图像(可选),根据自己的训练模型选择数据是否运行
  
  data_random_deal.py 对数据进行信息增强,包括锐化,模糊,噪声等,暂未整合到peopleTest整体目录架构运行
  
  remove_person_down_dir.py 删除不需要的目录下的每个病人的del_dir = [
    'CT_removal',
    'CT_enhancement_(-45~50)_interval=3',
    'PET_enhancement_(-45~50)_interval=3'

]
