import os
import shutil

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SOURCE_DIR = os.path.join(ROOT_DIR, "TextAsset")
DEST_DIR = os.path.join(ROOT_DIR, "rox-parser-main", "TextAsset")

# File mapping: source_name -> destination_name
# Use this to handle cases where source and destination names differ
FILE_MAPPING = {
  # Language files
  "cn_langs.bytes": "cn_langs.bytes",
  "en_langs.bytes": "en_langs.bytes",
  "in_langs.bytes": "in_langs.bytes",
  "th_langsnew.bytes": "th_langs.bytes",  # Source is th_langsnew.bytes, dest is th_langs.bytes
  "vn_langs.bytes": "vn_langs.bytes",
  
  # Game data files
  "data_AccumulativeMonth_AccumulativeMonth.bytes": "data_AccumulativeMonth_AccumulativeMonth.bytes",
  "data_area_Area.bytes": "data_area_Area.bytes",
  "data_AttrPoint.bytes": "data_AttrPoint.bytes",
  "data_AutoPoint.bytes": "data_AutoPoint.bytes",
  "data_baselevel.bytes": "data_baselevel.bytes",
  "data_BaseLevelGrowth.bytes": "data_BaseLevelGrowth.bytes",
  "data_dropV2_DropCollection.bytes": "data_dropV2_DropCollection.bytes",
  "data_dropV2_DropV2.bytes": "data_dropV2_DropV2.bytes",
  "data_EquipmentSmelting_EquipmentSmelting.bytes": "data_EquipmentSmelting_EquipmentSmelting.bytes",
  "data_EquipSlots.bytes": "data_EquipSlots.bytes",
  "data_equip_Appraisal.bytes": "data_equip_Appraisal.bytes",
  "data_equip_AppraisalLib.bytes": "data_equip_AppraisalLib.bytes",
  "data_equip_AttrPool.bytes": "data_equip_AttrPool.bytes",
  "data_equip_CardSuit.bytes": "data_equip_CardSuit.bytes",
  "data_equip_EnchantmentAttr.bytes": "data_equip_EnchantmentAttr.bytes",
  "data_equip_EnchantmentAttrLib.bytes": "data_equip_EnchantmentAttrLib.bytes",
  "data_equip_EnchantmentJob.bytes": "data_equip_EnchantmentJob.bytes",
  "data_equip_EnchantmentRandom.bytes": "data_equip_EnchantmentRandom.bytes",
  "data_equip_Equip.bytes": "data_equip_Equip.bytes",
  "data_equip_EquipmentDecomposition.bytes": "data_equip_EquipmentDecomposition.bytes",
  "data_equip_EquipmentFormula.bytes": "data_equip_EquipmentFormula.bytes",
  "data_equip_EquipmentRepair.bytes": "data_equip_EquipmentRepair.bytes",
  "data_equip_EquipmentSuit.bytes": "data_equip_EquipmentSuit.bytes",
  "data_equip_EquipmentType.bytes": "data_equip_EquipmentType.bytes",
  "data_equip_EquipRecommend.bytes": "data_equip_EquipRecommend.bytes",
  "data_equip_EquipRefineFx.bytes": "data_equip_EquipRefineFx.bytes",
  "data_equip_EquipSlots.bytes": "data_equip_EquipSlots.bytes",
  "data_equip_HeadwearAngle.bytes": "data_equip_HeadwearAngle.bytes",
  "data_equip_ItemCombine.bytes": "data_equip_ItemCombine.bytes",
  "data_equip_ItemSplit.bytes": "data_equip_ItemSplit.bytes",
  "data_equip_NpcSlot.bytes": "data_equip_NpcSlot.bytes",
  "data_equip_PropID.bytes": "data_equip_PropID.bytes",
  "data_equip_PunchHoleCost.bytes": "data_equip_PunchHoleCost.bytes",
  "data_equip_Refine.bytes": "data_equip_Refine.bytes",
  "data_equip_RefineSlotInherit.bytes": "data_equip_RefineSlotInherit.bytes",
  "data_equip_RemoveCardCost.bytes": "data_equip_RemoveCardCost.bytes",
  "data_equip_SlotStrengthen.bytes": "data_equip_SlotStrengthen.bytes",
  "data_equip_Suit.bytes": "data_equip_Suit.bytes",
  "data_GiftBoxV2.bytes": "data_GiftBoxV2.bytes",
  "data_Gifts_Gifts.bytes": "data_Gifts_Gifts.bytes",
  "data_InstanceGroup_InstanceGroup.bytes": "data_InstanceGroup_InstanceGroup.bytes",
  "data_ItemType.bytes": "data_ItemType.bytes",
  "data_ItemV2_ItemV2.bytes": "data_ItemV2_ItemV2.bytes",
  "data_item_CardCoordinates.bytes": "data_item_CardCoordinates.bytes",
  "data_item_CardCoordinatesAttr.bytes": "data_item_CardCoordinatesAttr.bytes",
  "data_item_CdGroup.bytes": "data_item_CdGroup.bytes",
  "data_joblevel.bytes": "data_joblevel.bytes",
  "data_JobReward.bytes": "data_JobReward.bytes",
  "data_job_Job.bytes": "data_job_Job.bytes",
  "data_lifeSkill_AreaDrop.bytes": "data_lifeSkill_AreaDrop.bytes",
  "data_lifeSkill_LifeLevel.bytes": "data_lifeSkill_LifeLevel.bytes",
  "data_lifeSkill_LifeProduce.bytes": "data_lifeSkill_LifeProduce.bytes",
  "data_lifeSkill_MineInfo.bytes": "data_lifeSkill_MineInfo.bytes",
  "data_lifeSkill_PlantInfo.bytes": "data_lifeSkill_PlantInfo.bytes",
  "data_monster_Monster.bytes": "data_monster_Monster.bytes",
  "data_Mount.bytes": "data_Mount.bytes",
  "data_mvpboss_MVP.bytes": "data_mvpboss_MVP.bytes",
  "data_npc_NPC.bytes": "data_npc_NPC.bytes",
  "data_npc_NPCIntimacy.bytes": "data_npc_NPCIntimacy.bytes",
  "data_Pendant.bytes": "data_Pendant.bytes",
  "data_pet_Pet.bytes": "data_pet_Pet.bytes",
  "data_pet_PetBaseAttr.bytes": "data_pet_PetBaseAttr.bytes",
  "data_pet_PetCatchingRate.bytes": "data_pet_PetCatchingRate.bytes",
  "data_pet_PetDecoration.bytes": "data_pet_PetDecoration.bytes",
  "data_pet_PetDecorationSet.bytes": "data_pet_PetDecorationSet.bytes",
  "data_pet_PetEvolution.bytes": "data_pet_PetEvolution.bytes",
  "data_pet_PetInitEndowment.bytes": "data_pet_PetInitEndowment.bytes",
  "data_pet_PetIntimacy.bytes": "data_pet_PetIntimacy.bytes",
  "data_pet_PetIntimacyItem.bytes": "data_pet_PetIntimacyItem.bytes",
  "data_pet_PetPotentiality.bytes": "data_pet_PetPotentiality.bytes",
  "data_pet_PetPotentialityRedistribute.bytes": "data_pet_PetPotentialityRedistribute.bytes",
  "data_pet_PetSkill.bytes": "data_pet_PetSkill.bytes",
  "data_pet_PetSkillGroup.bytes": "data_pet_PetSkillGroup.bytes",
  "data_pet_PetSkillTraining.bytes": "data_pet_PetSkillTraining.bytes",
  "data_Prop.bytes": "data_Prop.bytes",
  "data_PropCalculation.bytes": "data_PropCalculation.bytes",
  "data_scene_Scene.bytes": "data_scene_Scene.bytes",
  "data_SkillFactor.bytes": "data_SkillFactor.bytes",
  "data_skill_CommonSkill.bytes": "data_skill_CommonSkill.bytes",
  "data_skill_Skill.bytes": "data_skill_Skill.bytes",
  "data_skill_SkillRes.bytes": "data_skill_SkillRes.bytes",
  "data_Trade_Trade.bytes": "data_Trade_Trade.bytes",
}

# Copy files using the mapping
for source_file, dest_file in FILE_MAPPING.items():
  source_path = os.path.join(SOURCE_DIR, source_file)
  dest_path = os.path.join(DEST_DIR, dest_file)
  
  if os.path.exists(source_path):
    shutil.copy(source_path, dest_path)
    print(f"✓ Copied: {source_file} -> {dest_file}")
  else:
    print(f"✗ Source file not found: {source_file}")