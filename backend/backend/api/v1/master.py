from fastapi import APIRouter

from dependencies.auth import CurrentUserDep, CurrentMasterDep
from dependencies.masters import MasterServiceDep
from schemas.masters import MasterUpdate

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
    "me/working-hours"
)
async def get_working_hours():
    pass




@router.patch(
    "me/working-hours"
)
async def update_working_hours():
    pass




@router.get(
    "me/time-off"
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