console command for special hullmods
{
shuallhullmods
}
void hyperspaceCleanup(StarSystemAPI system)

SectorEntityToken addJumpPoint(
            String id,
            String name,
            @Nullable SectorEntityToken linkedPlanet,
            SectorEntityToken orbitCenter,
            float orbitStartAngle,
            float orbitRadius,
            float orbitDays
    )

MarketAPI addSimpleMarket(
            SectorEntityToken entity,
            String id,
            String name,
            Integer size,
            String faction,
            boolean isFreeport,
            boolean isHidden,            
            List <String> conditions,
            List <String> industries,            
            boolean hasStorage,
            boolean paidForStorage,
            boolean hasBlackmarket,
            boolean hasOpenmarket,
            boolean hasMilitarymarket,
            boolean isAbandonedStation


    )

conditions: list of conditions that can be fetched from campaign.ids.Conditions
industries: list of industries that can be fetched from campaign.ids.Industries
hasStorage
paidForStorage: is storage already freely available or has to be unlocked



Global.getSector().getEconomy().addMarket(market);

PersonAPI addCustomPerson(
            MarketAPI market,
            String firstName,
            String lastName,
            String portraitId,
            FullName.Gender gender,
            String factionId,
            String rankId,
            String postId,
            boolean isMarketAdmin,
            Integer industrialPlanning_level,
            Integer fleetLogistic_level,
            Integer planetaryOperations_level,
            Integer commScreenPosition
    )


market: MarketAPI the person is added to
firstName: person's first name
lastName: person's last name
portraitId: id of the sprite in settings.json/graphics/characters
gender: FullName.Gender value
factionId: person's faction
rankId: rank from campaign.ids.Ranks
postId: post from campaign.ids.Ranks
isMarketAdmin
industrialPlanning_level: skill level for market admin
fleetLogistic_level: skill level for market admin
planetaryOperations_level: skill level for market admin
commScreenPosition: position order in the comm screen, 0 being the admin position



SectorEntityToken createFleetBuilder()
  .setFleetName(String fleetName)
  .setFleetFaction(String fleetFaction)
  .setFleetType(@Nullable String fleetType)
  .setFlagshipName(@Nullable String flagshipName)
  .setFlagshipVariant(String flagshipVariant)
  .setFlagshipAlwaysRecoverable(boolean flagshipAlwaysRecoverable)
  .setFlagshipAutofit(boolean flagshipAutofit)
  .setCaptain(@Nullable PersonAPI captain)
  .setSupportFleet(@Nullable Map<String, Integer> supportFleet)
  .setSupportAutofit(boolean supportAutofit)
  .setMinFP(int minFP)
  .setReinforcementFaction(String reinforcementFaction)
  .setQualityOverride(@Nullable Float qualityOverride)
  .setSpawnLocation(@Nullable SectorEntityToken spawnLocation)
  .setAssignment(@Nullable FleetAssignment assignment)
  .setAssignmentTarget(@Nullable SectorEntityToken assignmentTarget)
  .setIsImportant(boolean isImportant)
  .setTransponderOn(boolean transponderOn)
  .setVariantsPath(@Nullable String variantsPath)
  .create();



fleetName: Default: "<faction name> Fleet".
fleetFaction: Default: MagicVariables.BOUNTY_FACTION ("ML_bounty").
fleetType: campaign.ids.FleetTypes, defaults to FleetTypes.PERSON_BOUNTY_FLEET.
flagshipName: Default: automatically picked by the game.
flagshipVariant: Default: picks the first ship in the fleet after it has been sorted.
flagshipAlwaysRecoverable: Default: false.
flagshipAutofit: Whether the flagship will be autofitted. When false, the Flagship does not receive D-mods or S-mods from the quality override. Default: false.
captain: PersonAPI, can be NULL for random captain, otherwise use MagicCampaign.createCaptainBuilder() .
supportFleet: Optional escort fleet, map with key=ships variants, values=number of ships with that variant. Default: no preset support fleet.
supportAutofit: Whether the preset ships will be autofitted. When false, the preset ships do not receive D-mods or S-mods from the quality override. Default: false.
minFP: Minimal fleet size, can be used to adjust to the player's power or simply add a random escort fleet. Set to 0 to ignore. Default: 0.
reinforcementFaction: if the fleet faction is a "neutral" one without ships in its doctrine, ships from a different faction can be picked as reinforcements . Default: fleetFaction.
qualityOverride: Optional ship quality override, default to 2 (no D-mods) if NULL or <0.
spawnLocation: Where the fleet will spawn, default to assignmentTarget if NULL.
assignment: campaign.FleetAssignment order, default to orbit_aggressive.
assignmentTarget: Where the fleet will go to execute its order. Default: spawnLocation. If spawnLocation is also not set, the fleet will not be spawned.
isImportant: will the fleet be tagged with a "!" in the campaign map, also prevents despawning. Default: false.
transponderOn: Default: false.


PersonAPI MagicCampaign.createCaptainBuilder()
  .setIsAI(boolean isAI)
  .setAICoreType(@Nullable String aiCoreType)
  .setFirstName(@Nullable String firstName)
  .setLastName(@Nullable String lastName)
  .setPortraitId(@Nullable String portraitId)
  .setGender(@Nullable FullName.Gender gender)
  .setFactionId(@NotNull String factionId)
  .setRankId(@Nullable String rankId)
  .setPostId(@Nullable String postId)
  .setPersonality(@Nullable String personality)
  .setLevel(@Nullable Integer level)
  .setEliteSkillsOverride(@Nullable Integer eliteSkillsOverride)
  .setSkillPreference(@Nullable OfficerManagerEvent.SkillPickPreference skillPreference)
  .setSkillLevels(@Nullable Map<String, Integer> skillLevels)
  .create();

isAI: Default: false
AICoreType: AI core from campaign.ids.Commodities. Default: none.
firstName: Default: randomly chosen from faction names.
lastName: Default: randomly chosen from faction names.
portraitId: id of the sprite in settings.json/graphics/characters. Default: randomly chosen from faction.
gender: Default: Randomly chosen between male and female if non-AI. Gender.ANY if AI.
factionId: Captain's faction id. Default: set in constructor.
rankId: rank from campaign.ids.Ranks. Default: Ranks.SPACE_COMMANDER'.
postId: post from campaign.ids.Ranks. Default:Ranks.POST_FLEET_COMMANDER.
personality: personality from campaign.ids.Personalities. Default: randomly chosen.
level: Captain's level, will pick random skills according to the faction's doctrine. Default: Set from skillLevels if present. If skillLevels is not set, 1 is used.
eliteSkillsOverride: Overrides the regular number of elite skills, set to -1 to ignore. Default: none.
skillPreference: GENERIC, PHASE, CARRIER, ANY from OfficerManagerEvent.SkillPickPreference. Default: OfficerManagerEvent.SkillPickPreference.ANY.
skillLevels: Map <skill, level> Optional Skills from campaign.ids.Skills and their appropriate levels, OVERRIDES ALL RANDOM SKILLS PREVIOUSLY PICKED! Default: none.




createDerelict(
	shipCondition = ShipRecoverySpecial.ShipCondition.GOOD;

)

	INSTRUCTION FOR SOUNDS.JSON FILES
	#Misc	
	#Hullmod Conflict WUB WUB
	"spuhm_hullmod_conflict":{
		"sounds":[
			{"file":"sounds/misc/spuhm_hullmod_conflict.ogg", "pitch":1, "volume":0.6},
			],
	},