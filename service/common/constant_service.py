from service.base_service import BaseService


class ConstantService(BaseService):
    """一些常量"""
    def __init__(self):
        self.STATE_TYPE_START = 1  # 开始
        self.STATE_TYPE_END = 2  # 结束   distribute_type_id

        self.STATE_DISTRIBUTE_TYPE_ACTIVE = 1  # 主动接单
        self.STATE_DISTRIBUTE_TYPE_RANDOM = 2  # 随机分配
        self.STATE_DISTRIBUTE_TYPE_ALL = 3  # 全部处理

        self.PARTICIPANT_TYPE_PERSONAL = 1  # 个人
        self.PARTICIPANT_TYPE_MULTI = 2  # 多人
        self.PARTICIPANT_TYPE_DEPT = 3  # 部门
        self.PARTICIPANT_TYPE_ROLE = 4  # 角色
        self.PARTICIPANT_TYPE_VARIABLE = 5  # 变量
        self.PARTICIPANT_TYPE_ROBOT = 6  # 机器人，脚本
        self.PARTICIPANT_TYPE_FIELD = 7  # 工单字段(用户名类型的)
        self.PARTICIPANT_TYPE_PARENT_FIELD = 8  # 父工单字段(用户名类型的)

        self.TRANSITION_TYPE_COMMON = 1  # 常规流转
        self.TRANSITION_TYPE_TIMER = 2  # 定时器流转

        self.FIELD_TYPE_STR = 5  # 字符串类型
        self.FIELD_TYPE_INT = 10  # 整形类型
        self.FIELD_TYPE_FLOAT = 15  # 浮点类型
        self.FIELD_TYPE_BOOL = 20  # 布尔类型
        self.FIELD_TYPE_DATE = 25  # 日期类型
        self.FIELD_TYPE_DATETIME = 30  # 日期时间类型
        self.FIELD_TYPE_RADIO = 35  # 单选框
        self.FIELD_TYPE_CHECKBOX = 40  # 多选框
        self.FIELD_TYPE_SELECT = 45  # 下拉列表
        self.FIELD_TYPE_MULTI_SELECT = 50  # 多选下拉列表
        self.FIELD_TYPE_TEXT = 55  # 文本域
        self.FIELD_TYPE_USERNAME = 60  # 用户名

        self.FIELD_ATTRIBUTE_RO = 1  # 只读
        self.FIELD_ATTRIBUTE_REQUIRED = 2  # 必填
        self.FIELD_ATTRIBUTE_OPTIONAL = 3  # 可选

        self.TICKET_PERMISSION_HANDLE = 1  # 处理权限
        self.TICKET_PERMISSION_VIEW = 2  # 查看权限

        self.TICKET_BASE_FIELD_LIST = ['id', 'sn', 'title', 'state_id', 'parent_ticket_id', 'parent_ticket_state_id',
                                       'participant_type_id', 'participant', 'workflow_id', 'ticket_type_id',
                                       'creator', 'is_deleted', 'created_at', 'updated_at']


CONSTANT_SERVICE = ConstantService()
