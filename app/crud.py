from sqlalchemy.orm import Session

import schemas
from models import fish as FishModel


def get_fish(db: Session, fish_id: int):
    return db.query(FishModel).filter(FishModel.Fish.id == fish_id).first()


def create_fish_data(db: Session, fish: schemas.Fish):
    new_entry = FishModel.Fish(
        date=fish.date,
        facility_ref_number=fish.facility_ref_number,
        licence_holder=fish.licence_holder,
        site_name=fish.site_name,
        fish_health_zone=fish.fish_health_zone,
        # counts_performed=fish.counts_performed
    )
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry
