import subprocess
import os

"""
`json_serializer_template_basic.lua` is a basic template that only contains the basic structure of the lua file. Meanwhile the `json_serialuizer_template.lua` is a more complex template that contains the basic structure and the `__default_values` function that is used to set the default values of the table. To run the script with the basic template, uncomment the `TEMPLATE_FILE_NAME` variable and comment the `TEMPLATE_FILE_NAME` variable that is used to run the script with the complex template.
"""

# TEMPLATE_FILE_NAME = f"json_serializer_template_basic.lua"
TEMPLATE_FILE_NAME = f"json_serializer_template.lua"

TARGET_FILES = [
  "data_dropV2_DropV2.bytes",
  "data_dropV2_DropCollection.bytes",
  "data_equip_EquipmentSuit.bytes",
  "data_equip_Equip.bytes",
  "data_equip_Refine.bytes",
  "data_equip_ItemSplit.bytes",
  "data_equip_ItemCombine.bytes",
  "data_item_Item.bytes",
  "data_item_CardCoordinates.bytes",
  "data_item_CardCoordinatesAttr.bytes",
  "data_item_CdGroup.bytes",
  "data_EquipSlots.bytes",
  "data_equip_Appraisal.bytes",
  "data_equip_AppraisalLib.bytes",
  "data_equip_AttrPool.bytes",
  "data_equip_CardSuit.bytes",
  "data_equip_EnchantmentAttr.bytes",
  "data_equip_EnchantmentAttrLib.bytes",
  "data_equip_EnchantmentJob.bytes",
  "data_equip_EnchantmentRandom.bytes",
  "data_equip_Equip.bytes",
  "data_equip_EquipmentDecomposition.bytes",
  "data_equip_EquipmentFormula.bytes",
  "data_equip_EquipmentRepair.bytes",
  "data_equip_EquipmentSuit.bytes",
  "data_equip_EquipmentType.bytes",
  "data_equip_EquipRecommend.bytes",
  "data_equip_EquipRefineFx.bytes",
  "data_equip_EquipSlots.bytes",
  "data_equip_HeadwearAngle.bytes",
  "data_equip_ItemCombine.bytes",
  "data_equip_ItemSplit.bytes",
  "data_equip_NpcSlot.bytes",
  "data_equip_PropID.bytes",
  "data_equip_PunchHoleCost.bytes",
  "data_equip_Refine.bytes",
  "data_equip_RefineSlotInherit.bytes",
  "data_equip_RemoveCardCost.bytes",
  "data_equip_SlotStrengthen.bytes",
  "data_equip_Suit.bytes",
  "data_EquipmentSmelting_EquipmentSmelting.bytes",
  "data_monster_Monster.bytes",
  "data_area_Area.bytes",
  "data_AccumulativeMonth_AccumulativeMonth.bytes",
  "data_AttrPoint.bytes",
  "data_AutoPoint.bytes",
  "data_baselevel.bytes",
  "data_BaseLevelGrowth.bytes",
  "data_equip_Appraisal.bytes",
  "data_equip_AppraisalLib.bytes",
  "data_equip_EquipmentDecomposition.bytes",
  "data_equip_EquipmentRepair.bytes",
  "data_equip_EquipmentSuit.bytes",
  "data_equip_EquipmentType.bytes",
  "data_equip_ItemCombine.bytes",
  "data_equip_ItemSplit.bytes",
  "data_equip_PropID.bytes",
  "data_equip_Refine.bytes",
  "data_equip_SlotStrengthen.bytes",
  "data_EquipmentSmelting_EquipmentSmelting.bytes",
  "data_GiftBoxV2.bytes",
  "data_Gifts_Gifts.bytes",
  "data_InstanceGroup_InstanceGroup.bytes",
  "data_item_CardCoordinatesAttr.bytes",
  "data_ItemType.bytes",
  "data_job_Job.bytes",
  "data_joblevel.bytes",
  "data_JobReward.bytes",
  "data_lifeSkill_AreaDrop.bytes",
  "data_lifeSkill_LifeLevel.bytes",
  "data_lifeSkill_LifeProduce.bytes",
  "data_lifeSkill_MineInfo.bytes",
  "data_lifeSkill_PlantInfo.bytes",
  "data_Mount.bytes",
  "data_mvpboss_MVP.bytes",
  "data_npc_NPC.bytes",
  "data_npc_NPCIntimacy.bytes",
  "data_Pendant.bytes",
  "data_pet_Pet.bytes",
  "data_pet_PetEvolution.bytes",
  "data_pet_PetCatchingRate.bytes",
  "data_pet_PetIntimacy.bytes",
  "data_pet_PetIntimacyItem.bytes",
  "data_pet_PetPotentiality.bytes",
  "data_pet_PetPotentialityRedistribute.bytes",
  "data_pet_PetSkill.bytes",
  "data_pet_PetSkillGroup.bytes",
  "data_pet_PetSkillTraining.bytes",
  "data_Prop.bytes",
  "data_PropCalculation.bytes",
  "data_skill_CommonSkill.bytes",
  "data_skill_Skill.bytes",
  "data_skill_SkillRes.bytes",
  "data_SkillFactor.bytes",
  "data_Trade_Trade.bytes",
  "data_scene_Scene.bytes",
  "data_pet_PetBaseAttr.bytes",
  "data_pet_PetDecoration.bytes",
  "data_pet_PetDecorationSet.bytes",
  "data_pet_PetInitEndowment.bytes",
]


if not os.path.exists("JSON"):
  os.makedirs("JSON")

for TARGET_FILE in TARGET_FILES:
  FILE_NAME = TARGET_FILE.replace("data_", "").replace(".bytes", "")
  TITLE = TARGET_FILE.replace(".bytes", "")

  TABLE = []
  with open(f"20240618/TextAssets/{TARGET_FILE}", "r", encoding="utf8") as filename:
    contents = filename.readlines()

    for content in contents:
      if content.startswith("do") or content.startswith("for _,v"):
        break

      if f"return {FILE_NAME}" not in content and f"{FILE_NAME}.funcNew=function()end;" not in content and f"return table;" not in content:
        TABLE.append(content)
      else:
        pass
      

  # with open(f"json_serializer_template.lua", "r", encoding="utf8") as filename:
  with open(TEMPLATE_FILE_NAME, "r", encoding="utf8") as filename:
    TEMPLATE = filename.readlines()

  FINAL_LUA = []
  
  # to_replace = """
  # do
  #   local base = { __index = __default_values, __newindex = function() error( "Attempt to modify read-only table" ) end }
  #   for k, v in pairs( """ + FILE_NAME + """ ) do
  #     setmetatable( v, base )
  #   end
  #   base.__metatable = false
  # end
  # """

  # print(to_replace)

  # TABLE = "".join(TABLE).replace("to_replace", "")
  TABLE = "".join(TABLE)

  for line in TEMPLATE:
    line = line.replace("{{TABLE}}", TABLE)
    line = line.replace("{{FILE_NAME}}", FILE_NAME)
    line = line.replace("{{TITLE}}", TITLE)

    FINAL_LUA.append(line)

  with open(f"json_serializer.lua", "w", encoding="utf8") as filename:
    filename.writelines(FINAL_LUA)

  subprocess.call("lua json_serializer.lua", shell=True)