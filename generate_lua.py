import subprocess
import os

"""
`json_serializer_template_basic.lua` is a basic template that only contains the basic structure of the lua file. Meanwhile the `json_serialuizer_template.lua` is a more complex template that contains the basic structure and the `__default_values` function that is used to set the default values of the table. To run the script with the basic template, uncomment the `TEMPLATE_FILE_NAME` variable and comment the `TEMPLATE_FILE_NAME` variable that is used to run the script with the complex template.
"""

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
SOURCE_DIR = os.path.join(ROOT_DIR, "TextAsset")
OUTPUT_DIR = os.path.join(ROOT_DIR, "JSON")
LOCAL_LUA = os.path.join(ROOT_DIR, "tools", "lua", "bin", "lua.exe")

# TEMPLATE_FILE_NAME = f"json_serializer_template_basic.lua"
TEMPLATE_FILE_NAME = f"json_serializer_template.lua"
TEMPLATE_PATH = os.path.join(ROOT_DIR, TEMPLATE_FILE_NAME)

TARGET_FILES = [
  "data_AccumulativeMonth_AccumulativeMonth.bytes",
  "data_AttrPoint.bytes",
  "data_AutoPoint.bytes",
  "data_BaseLevelGrowth.bytes",
  "data_EquipSlots.bytes",
  "data_EquipmentSmelting_EquipmentSmelting.bytes",
  "data_GiftBoxV2.bytes",
  "data_Gifts_Gifts.bytes",
  "data_InstanceGroup_InstanceGroup.bytes",
  "data_ItemType.bytes",
  "data_ItemV2_ItemV2.bytes",
  "data_JobReward.bytes",
  "data_Mount.bytes",
  "data_Pendant.bytes",
  "data_Prop.bytes",
  "data_PropCalculation.bytes",
  "data_SkillFactor.bytes",
  "data_Trade_Trade.bytes",
  "data_area_Area.bytes",
  "data_baselevel.bytes",
  "data_dropV2_DropCollection.bytes",
  "data_dropV2_DropV2.bytes",
  "data_equip_Appraisal.bytes",
  "data_equip_AppraisalLib.bytes",
  "data_equip_AttrPool.bytes",
  "data_equip_CardSuit.bytes",
  "data_equip_EnchantmentAttr.bytes",
  "data_equip_EnchantmentAttrLib.bytes",
  "data_equip_EnchantmentJob.bytes",
  "data_equip_EnchantmentRandom.bytes",
  "data_equip_Equip.bytes",
  "data_equip_EquipRecommend.bytes",
  "data_equip_EquipRefineFx.bytes",
  "data_equip_EquipSlots.bytes",
  "data_equip_EquipmentDecomposition.bytes",
  "data_equip_EquipmentFormula.bytes",
  "data_equip_EquipmentRepair.bytes",
  "data_equip_EquipmentSuit.bytes",
  "data_equip_EquipmentType.bytes",
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
  "data_item_CardCoordinates.bytes",
  "data_item_CardCoordinatesAttr.bytes",
  "data_item_CdGroup.bytes",
  "data_job_Job.bytes",
  "data_joblevel.bytes",
  "data_lifeSkill_AreaDrop.bytes",
  "data_lifeSkill_LifeLevel.bytes",
  "data_lifeSkill_LifeProduce.bytes",
  "data_lifeSkill_MineInfo.bytes",
  "data_lifeSkill_PlantInfo.bytes",
  "data_monster_Monster.bytes",
  "data_mvpboss_MVP.bytes",
  "data_npc_NPC.bytes",
  "data_npc_NPCIntimacy.bytes",
  "data_pet_Pet.bytes",
  "data_pet_PetBaseAttr.bytes",
  "data_pet_PetCatchingRate.bytes",
  "data_pet_PetDecoration.bytes",
  "data_pet_PetDecorationSet.bytes",
  "data_pet_PetEvolution.bytes",
  "data_pet_PetInitEndowment.bytes",
  "data_pet_PetIntimacy.bytes",
  "data_pet_PetIntimacyItem.bytes",
  "data_pet_PetPotentiality.bytes",
  "data_pet_PetPotentialityRedistribute.bytes",
  "data_pet_PetSkill.bytes",
  "data_pet_PetSkillGroup.bytes",
  "data_pet_PetSkillTraining.bytes",
  "data_scene_Scene.bytes",
  "data_skill_CommonSkill.bytes",
  "data_skill_Skill.bytes",
  "data_skill_SkillRes.bytes",
]


if not os.path.exists(OUTPUT_DIR):
  os.makedirs(OUTPUT_DIR)

for TARGET_FILE in TARGET_FILES:
  FILE_NAME = TARGET_FILE.replace("data_", "").replace(".bytes", "")
  TITLE = TARGET_FILE.replace(".bytes", "")

  TABLE = []
  with open(os.path.join(SOURCE_DIR, TARGET_FILE), "r", encoding="utf8") as filename:
    contents = filename.readlines()

  # If file starts with `return`, convert to a named table assignment
  first_non_empty = next((line for line in contents if line.strip()), "")
  if first_non_empty.lstrip().startswith("return"):
    raw = "".join(contents)
    stripped = raw.lstrip()
    table_body = stripped[len("return"):].lstrip()
    TABLE = f"local {FILE_NAME} = {table_body}"
  else:
    for content in contents:
      if content.lstrip().startswith("do") or content.lstrip().startswith("for _,v"):
        break

      if f"return {FILE_NAME}" not in content and f"{FILE_NAME}.funcNew=function()end;" not in content and f"return table;" not in content:
        TABLE.append(content)
      

  # with open(f"json_serializer_template.lua", "r", encoding="utf8") as filename:
  with open(TEMPLATE_PATH, "r", encoding="utf8") as filename:
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
  if isinstance(TABLE, list):
    TABLE = "".join(TABLE)

  if "__default_values" not in TABLE:
    TABLE = "local __default_values = {}\n" + TABLE

  if f"local {FILE_NAME}" not in TABLE and f"{FILE_NAME} =" not in TABLE:
    if "local table" in TABLE or "table =" in TABLE:
      TABLE = TABLE + f"\nlocal {FILE_NAME} = table\n"

  for line in TEMPLATE:
    line = line.replace("{{TABLE}}", TABLE)
    line = line.replace("{{FILE_NAME}}", FILE_NAME)
    line = line.replace("{{TITLE}}", TITLE)

    FINAL_LUA.append(line)

  with open(os.path.join(ROOT_DIR, "json_serializer.lua"), "w", encoding="utf8") as filename:
    filename.writelines(FINAL_LUA)

  if os.path.exists(LOCAL_LUA):
    subprocess.call([LOCAL_LUA, "json_serializer.lua"], cwd=ROOT_DIR)
  else:
    subprocess.call("lua json_serializer.lua", shell=True)
