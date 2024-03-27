from paychex_python_sdk.paths.workers_worker_id.get import ApiForget
from paychex_python_sdk.paths.workers_worker_id.delete import ApiFordelete
from paychex_python_sdk.paths.workers_worker_id.patch import ApiForpatch


class WorkersWorkerId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
