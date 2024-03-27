from paychex_python_sdk.paths.management_hooks.get import ApiForget
from paychex_python_sdk.paths.management_hooks.post import ApiForpost


class ManagementHooks(
    ApiForget,
    ApiForpost,
):
    pass
