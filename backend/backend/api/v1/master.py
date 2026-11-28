from fastapi import APIRouter

from dependencies.auth import CurrentMasterDep
from dependencies.masters import MasterServiceDep
from schemas.masters import MasterUpdate
from schemas.time_off import TimeOffRead
from schemas.working_schema import WorkingHoursSchema
from services.working_hours import WorkingHoursService

router = APIRouter(
    prefix="/masters",
    tags=["masters"],
)



@router.get(
    "me/bookings"
)
async def get_my_bookings():
    pass




@router.post(
    "/me/bookings/{booking_id}/complete"
)
async def complete_booking():
    pass




@router.get(
    "/me/working-hours",
    response_model=WorkingHoursSchema
)
async def get_working_hours(
        master: CurrentMasterDep,
        service: WorkingHoursService
):
    return await service.get_master_working_hours(master.id)



@router.patch(
    "/me/working-hours"
)
async def update_working_hours(
        master: CurrentMasterDep,
        body: WorkingHoursSchema,
        service: WorkingHoursService
):
    await service.update_working_hours(master.id, body)




@router.get(
    "/me/time-off",
    response_model=list[TimeOffRead]
)
async def get_time_off():
    pass




@router.post(
    "/me/time-off"
)
async def create_time_off():
    pass



@router.delete(
    "/me/time-off/{time_off_id}"
)
async def delete_time_off():
    pass


@router.get("/me")
async def get_me(
        current_master: CurrentMasterDep
):
    return current_master


@router.patch("/me")
async def patch_me(
        current_master: CurrentMasterDep,
        body: MasterUpdate,
        service: MasterServiceDep
):
    await service.master_update(current_master.id, body)