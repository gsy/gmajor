
import attr


@attr.s
class ApiResult(object):
    code = attr.ib(default=200)
    msg = attr.ib(default='')
    data = attr.ib(default={})
