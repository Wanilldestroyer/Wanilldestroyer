package data.scripts.world.systems;

import java.awt.Color;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.concurrent.locks.Condition;

import com.fs.starfarer.api.Global;
import com.fs.starfarer.api.campaign.*;
import com.fs.starfarer.api.campaign.econ.EconomyAPI;
import com.fs.starfarer.api.campaign.econ.MarketAPI;
import com.fs.starfarer.api.characters.PersonAPI;
import com.fs.starfarer.api.impl.campaign.ids.*;
import com.fs.starfarer.api.impl.campaign.procgen.NebulaEditor;
import com.fs.starfarer.api.impl.campaign.procgen.PlanetConditionGenerator;
import com.fs.starfarer.api.impl.campaign.procgen.StarAge;
import com.fs.starfarer.api.impl.campaign.procgen.StarSystemGenerator;
import com.fs.starfarer.api.impl.campaign.terrain.AsteroidFieldTerrainPlugin.AsteroidFieldParams;
import com.fs.starfarer.api.impl.campaign.terrain.HyperspaceTerrainPlugin;
import com.fs.starfarer.api.util.Misc;
import com.fs.starfarer.api.impl.campaign.terrain.MagneticFieldTerrainPlugin.MagneticFieldParams;
import org.lazywizard.lazylib.MathUtils;
import exerelin.campaign.SectorManager;
import data.scripts.world.systems.MyModPlugin;

public class RedDragon {
    public void generate(SectorAPI sector) {

        StarSystemAPI system = sector.createStarSystem("My Star");
        system.getLocation().set(12000,14000); //Halftop center

        system.setBackgroundTextureFilename("graphics/backgrounds/background5.jpg");
    }
// create the star and generate the hyperspace anchor for this system
public static String getName()
	{
PlanetAPI argonStar = system.initStar("Argon", // unique id for this star
        "star_white", // id in planets.json
        1500f, // radius (in pixels at default zoom)
        450); // corona radius, from star edge
system.setLightColor(new Color(239, 155, 128));
 // light color in entire system, affects all entities
//asteroid belt1 ring
system.addAsteroidBelt(argonStar, 1000, asteroidBelt1Dist, 800, 250, 400, Terrain.ASTEROID_BELT, "Inner Band");
        }
public static MarketAPI addMarketplace(String factionID, SectorEntityToken primaryEntity,
										   ArrayList<SectorEntityToken> connectedEntities, String name, int size,
										   ArrayList<String> conditionList, ArrayList<ArrayList<String>> industryList, ArrayList<String> submarkets,
										   float tarrif, boolean freePort) {
		EconomyAPI globalEconomy = Global.getSector().getEconomy();
		String planetID = primaryEntity.getId();
		String marketID = planetID/* + "_market"*/;

		MarketAPI newMarket = Global.getFactory().createMarket(marketID, name, size);
		newMarket.setFactionId(factionID);
		newMarket.setPrimaryEntity(primaryEntity);
		newMarket.getTariff().modifyFlat("generator", tarrif);
		newMarket.getLocationInHyperspace().set(primaryEntity.getLocationInHyperspace());

		if (null != submarkets) {
			for (String market : submarkets) {
				newMarket.addSubmarket(market);
			}
		}

		if (null != conditionList) {
			for (String condition : conditionList) {
				newMarket.addCondition(condition);
			}
		}

		for (ArrayList<String> industryWithParam : industryList) {
			String industry = industryWithParam.get(0);
			if (industryWithParam.size() == 1) {
				newMarket.addIndustry(industry);
			} else {
				newMarket.addIndustry(industry, industryWithParam.subList(1, industryWithParam.size()));
			}
		}

		if (null != connectedEntities) {
			for (SectorEntityToken entity : connectedEntities) {
				newMarket.getConnectedEntities().add(entity);
			}
		}

		newMarket.setFreePort(freePort);
		globalEconomy.addMarket(newMarket, false);
		primaryEntity.setMarket(newMarket);
		primaryEntity.setFaction(factionID);

		if (null != connectedEntities) {
			for (SectorEntityToken entity : connectedEntities) {
				entity.setMarket(newMarket);
				entity.setFaction(factionID);
			}
		}
		return newMarket;
	}
        public static void generatePt2(SectorAPI sector) {

		StarSystemAPI system = sector.getStarSystem(getName());
		SectorEntityToken heart = sector.getEntityById("NewZeland");
		//MarketAPI heartmarket = heart.getMarket();

		MarketAPI heartmarket = addMarketplace("enigma", heart,
				null,
				"RedDragon", 5, // 3 industry limit
				null,
				new ArrayList<>(Arrays.asList(
						new ArrayList<>(Arrays.asList(Industries.POPULATION, Commodities.ALPHA_CORE)),
						new ArrayList<>(Arrays.asList(Industries.SPACEPORT, Commodities.ALPHA_CORE)),
						new ArrayList<>(Arrays.asList(Industries.HIGHCOMMAND, Commodities.ALPHA_CORE)),
						new ArrayList<>(Arrays.asList(Industries.ORBITALWORKS, Items.PRISTINE_NANOFORGE, Commodities.ALPHA_CORE)), // Industry
						new ArrayList<>(Arrays.asList(Industries.FUELPROD, Commodities.ALPHA_CORE)),
						new ArrayList<>(Arrays.asList(Industries.LIGHTINDUSTRY, Commodities.ALPHA_CORE)),
						new ArrayList<>(Arrays.asList(Industries.HEAVYBATTERIES, Commodities.ALPHA_CORE)),
						new ArrayList<>(Arrays.asList(Industries.STARFORTRESS, Commodities.ALPHA_CORE)))),
				new ArrayList<String>(),
				0.3f,
				false
		);

		heartmarket.setHidden(true);
		heartmarket.setInvalidMissionTarget(true);
		heartmarket.setEconGroup(heartmarket.getId());

		heartmarket.addCondition(Conditions.POPULATION_5);
		heartmarket.addCondition(Conditions.OUTPOST);
		heartmarket.addCondition("nskr_enigmaPop");
		heartmarket.addCondition(Conditions.FRONTIER);
		heartmarket.addCondition(Conditions.COLD);
		heartmarket.addCondition(Conditions.RUINS_VAST);

		heartmarket.getMemoryWithoutUpdate().set("$nex_uninvadable", true);
		heartmarket.setSurveyLevel(MarketAPI.SurveyLevel.FULL);

		heartmarket.reapplyIndustries();

		heartmarket.getLocationInHyperspace().set(system.getLocation());

	}
        public static void generate(SectorAPI sector) {
		random.setSeed(sector.getSeedString().hashCode());

		StarSystemAPI system = sector.createStarSystem(getName());

		system.setLightColor(STAR_LIGHT_COLOR);
		system.setDoNotShowIntelFromThisLocationOnMap(true);
                PlanetAPI siberia = system.addPlanet("RED_siberia", star, "Siberia", "cryovolcanic", 10, 230, 8500, 750);

                //extra parts
                system.addAsteroidBelt(star, 150, 3500, 350, 450, 500, Terrain.ASTEROID_BELT, "Frozen Belt");
		system.addRingBand(star, "misc", "rings_ice0", 256f, 1, GLACIER_COLOR, 256f, 3500, 200f);
		system.addRingBand(star, "misc", "rings_ice0", 256f, 1, GLACIER_COLOR, 256f, 11000, 800f);

		JumpPointAPI jumpPoint = Global.getFactory().createJumpPoint("RED_frost_jumpPoint", getName() + " Jump-point");
		OrbitAPI orbit = Global.getFactory().createCircularOrbit(star, 230, 4500, 300);
		jumpPoint.setRelatedPlanet(glacier);
		jumpPoint.setOrbit(orbit);
		jumpPoint.setStandardWormholeToHyperspaceVisual();
		system.addEntity(jumpPoint);
        }
    // Argon Gamma: Dead World
PlanetAPI argonGamma = system.addPlanet("argon_RED",
        argonStar,
        "Argon Gamma V",
        "barren-Desert",
        360f * (float) Math.random(),
        320f,
        argonGammaDist,
        1421f);
argonGamma.setCustomDescriptionId("redlegion_argon_argonGamma"); //reference descriptions.csv
PlanetConditionGenerator.generateConditionsForPlanet(argonGamma, StarAge.AVERAGE);

// Argon Prime: Terran homeworld
PlanetAPI argonPrime = system.addPlanet("argon_prime",
        argonStar,
        "Argon Prime",
        "terran",
        360f * (float) Math.random(),
        220f,
        argonPrimeDist,
        320f);

argonPrime.setCustomDescriptionId("redlegion_argon_argonprime"); //reference descriptions.csv

MarketAPI argonPrime_market = addMarketplace("redlegion", argonPrime, null,
        "Argon Prime",
        6,
        Arrays.asList(
                Conditions.POPULATION_6,
                Conditions.ORE_RICH,
                Conditions.RARE_ORE_ABUNDANT,
                Conditions.FARMLAND_BOUNTIFUL,
                Conditions.HABITABLE,
                Conditions.ORGANIZED_CRIME,
                Conditions.TERRAN,
                Conditions.REGIONAL_CAPITAL,
                Conditions.STEALTH_MINEFIELDS,
                Conditions.AI_CORE_ADMIN
        ),
        Arrays.asList(
                Submarkets.GENERIC_MILITARY,
                Submarkets.SUBMARKET_OPEN,
                Submarkets.SUBMARKET_STORAGE,
                Submarkets.SUBMARKET_BLACK
        ),
        Arrays.asList(
                Industries.POPULATION,
                Industries.MEGAPORT,
                Industries.MINING,
                Industries.STARFORTRESS,
                Industries.HEAVYBATTERIES,
                Industries.HIGHCOMMAND,
                Industries.WAYSTATION
        ),
        0.18f,
        true,
        true);

argonPrime_market.addIndustry(Industries.ORBITALWORKS, Collections.singletonList(Items.PRISTINE_NANOFORGE)); //couldn't find another way to add w/ forge!
argonPrime_market.getIndustry(Industries.HIGHCOMMAND).setAICoreId(Commodities.ALPHA_CORE);
argonPrime_market.getIndustry(Industries.STARFORTRESS).setAICoreId(Commodities.ALPHA_CORE);
argonPrime_market.getIndustry(Industries.MEGAPORT).setAICoreId(Commodities.ALPHA_CORE);
argonPrime_market.getIndustry(Industries.ORBITALWORKS).setAICoreId(Commodities.ALPHA_CORE);
argonPrime_market.getIndustry(Industries.POPULATION).setAICoreId(Commodities.BETA_CORE);
argonPrime_market.getIndustry(Industries.WAYSTATION).setAICoreId(Commodities.GAMMA_CORE);
    
    // Blood Keep - the Blood Knight Citadel: Far orbital near the fringe point for garrison, place where strike forces report back and regroup
SectorEntityToken bloodKeep = system.addCustomEntity("argon_blood_keep", "Blood Keep", "station_hightech2", "redlegion");
bloodKeep.setCircularOrbitPointingDown(argonStar, 0, bloodDist, 4000f);
bloodKeep.setCustomDescriptionId("redlegion_argon_bloodkeep");
MarketAPI bloodKeep_market = addMarketplace("redlegion", bloodKeep, null,
        "Blood Keep",
        4,
        Arrays.asList(
                Conditions.POPULATION_4,
                Conditions.NO_ATMOSPHERE,
                Conditions.OUTPOST,
                Conditions.AI_CORE_ADMIN
        ),
        Arrays.asList(
                Submarkets.GENERIC_MILITARY,
                Submarkets.SUBMARKET_STORAGE,
                Submarkets.SUBMARKET_BLACK
        ),
        Arrays.asList(
                Industries.POPULATION,
                Industries.SPACEPORT,
                Industries.BATTLESTATION_HIGH,
                Industries.HEAVYBATTERIES,
                Industries.MILITARYBASE,
                Industries.ORBITALWORKS,
                Industries.WAYSTATION
        ),
        0.18f,
        false,
        false);

bloodKeep_market.getIndustry(Industries.MILITARYBASE).setAICoreId(Commodities.BETA_CORE);
bloodKeep_market.getIndustry(Industries.BATTLESTATION_HIGH).setAICoreId(Commodities.ALPHA_CORE);
bloodKeep_market.getIndustry(Industries.ORBITALWORKS).setAICoreId(Commodities.BETA_CORE);

//jump point code
JumpPointAPI jumpPoint3 = Global.getFactory().createJumpPoint(
        "fringe_jump",
        "Fringe System Jump");

jumpPoint3.setCircularOrbit(system.getEntityById("Argon"), 2, jumpFringeDist, 4000f);
jumpPoint3.setStandardWormholeToHyperspaceVisual();

system.addEntity(jumpPoint3);


    
    }