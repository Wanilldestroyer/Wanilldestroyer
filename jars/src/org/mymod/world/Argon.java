package jars.src.org.mymod.world;

import com.fs.starfarer.api.Global;
import com.fs.starfarer.api.campaign.*;
import com.fs.starfarer.api.campaign.econ.EconomyAPI;
import com.fs.starfarer.api.campaign.econ.MarketAPI;
import com.fs.starfarer.api.impl.campaign.DerelictShipEntityPlugin;
import com.fs.starfarer.api.impl.campaign.ids.*;
import com.fs.starfarer.api.impl.campaign.procgen.*;
import com.fs.starfarer.api.impl.campaign.procgen.themes.BaseThemeGenerator;
import com.fs.starfarer.api.impl.campaign.procgen.themes.SalvageSpecialAssigner;
import com.fs.starfarer.api.impl.campaign.rulecmd.salvage.special.ShipRecoverySpecial;
import com.fs.starfarer.api.impl.campaign.terrain.BaseTiledTerrain;
import com.fs.starfarer.api.impl.campaign.terrain.HyperspaceTerrainPlugin;
import com.fs.starfarer.api.impl.campaign.terrain.MagneticFieldTerrainPlugin;
import com.fs.starfarer.api.util.Misc;
import org.lazywizard.lazylib.MathUtils;
import org.lwjgl.util.vector.Vector2f;

import java.awt.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;

public class Argon {
    public void generate(SectorAPI sector) {

        StarSystemAPI system = sector.createStarSystem("My Star");
        system.getLocation().set(12000,14000); //Halftop right

        system.setBackgroundTextureFilename("graphics/backgrounds/nskr_cache.jpg");
        
        PlanetAPI Argon_star = system.initStar("Argon_Star",
                "star_yellow",
                400f,
                700f);

         system.addRingBand(spindle_star, "misc", "rings_dust0", 256f, 2, Color.gray, 400f, 1600f, 200f);


        PlanetAPI Argon_1 = system.addPlanet("New_Argon_p01",
                Argon_star,
                "Weft",
                "lava_minor",
                360f*(float)Math.random(),
                140,
                2600,
                160);

        PlanetConditionGenerator.generateConditionsForPlanet(Argon_1, StarAge.YOUNG);

        PlanetAPI Argon_2 = system.addPlanet("New_Argon_p02",
                Argon_star,
                "Warp",
                "barren",
                360f*(float)Math.random(),
                180,
                4200,
                230);

        PlanetConditionGenerator.generateConditionsForPlanet(Argon_2, StarAge.YOUNG);

        SectorEntityToken stable1 = system.addCustomEntity("New_Argon_stableLoc1", "Stable Location", "stable_location", Factions.NEUTRAL);
        stableLoc1.setCircularOrbit(Argon_star, 360f*(float)Math.random(),3400, 400);
        PlanetAPI Argon_3 = system.addPlanet("New_Argon_char",
                Argon_star,
                "Char",
                "jungle",
                charAngle,
                190,
                8500,
                300);
        JumpPointAPI jumpPointChar = Global.getFactory().createJumpPoint("New_Argon_char_jump", "Spinner's Road");
        jumpPointCharkha.setCircularOrbit(Argon_star, charAngle+30, 8000, 300);
        jumpPointCharkha.setRelatedPlanet(Argon_3);
        system.addEntity(jumpPointChar);

        MarketAPI Argon_3_market = addMarketplace("RedDragon", Argon_3, null,
                "Char",
                7,
                new ArrayList<>(
                        Arrays.asList(
                                Conditions.POPULATION_7,
                                Conditions.HABITABLE,
                                Conditions.FARMLAND_ADEQUATE,
                                Conditions.ORGANICS_COMMON,
                                Conditions.ORE_SPARSE,
                                Conditions.INIMICAL_BIOSPHERE,
                                Conditions.REGIONAL_CAPITAL,
                                "New_gatescar"
                        )
                ),
                new ArrayList<>(
                        Arrays.asList(
                                Submarkets.SUBMARKET_OPEN,
                                Submarkets.GENERIC_MILITARY,
                                "New_stdfmarket",
                                Submarkets.SUBMARKET_BLACK,
                                Submarkets.SUBMARKET_STORAGE
                        )
                ),
                new ArrayList<>(
                        Arrays.asList(
                                Industries.POPULATION,
                                Industries.MEGAPORT,
                                Industries.MINING,
                                Industries.FARMING,
                                Industries.STARFORTRESS_HIGH,
                                Industries.HEAVYBATTERIES,
                                Industries.HIGHCOMMAND,
                                "New_RedDragon"
                        )
                ),
                0.3f,
                false,
                true);

        spindle_3_market.addIndustry(Industries.ORBITALWORKS,new ArrayList<String>(Arrays.asList(Items.CORRUPTED_NANOFORGE)));
        spindle_3_market.getIndustry(Industries.HIGHCOMMAND).setAICoreId(Commodities.ALPHA_CORE);
        spindle_3_market.getIndustry(Industries.STARFORTRESS_HIGH).setAICoreId(Commodities.ALPHA_CORE);

        float radiusAfter = StarSystemGenerator.addOrbitingEntities(system, Argon_star, StarAge.YOUNG,
                2, 3, // min/max entities to add
                15000, // radius to start adding at
                0, // name offset - next planet will be <system name> <roman numeral of this parameter + 1>
                true); // whether to use custom or system-name based names

    }

    private void cleanup(StarSystemAPI system){
        HyperspaceTerrainPlugin plugin = (HyperspaceTerrainPlugin) Misc.getHyperspaceTerrain().getPlugin();
        NebulaEditor editor = new NebulaEditor(plugin);
        float minRadius = plugin.getTileSize() * 2f;

        float radius = system.getMaxRadiusInHyperspace();
        editor.clearArc(system.getLocation().x, system.getLocation().y, 0, radius + minRadius * 0.5f, 0f, 360f);
        editor.clearArc(system.getLocation().x, system.getLocation().y, 0, radius + minRadius, 0f, 360f, 0.25f);
    }

    public static MarketAPI addConditionMarket(SectorEntityToken entity, ArrayList<String> marketConditions)
    {
        String planetID = entity.getId();
        String marketID = planetID + "_market";

        MarketAPI newMarket = Global.getFactory().createMarket(marketID, entity.getName(), 0);
        newMarket.setPrimaryEntity(entity);
        newMarket.setPlanetConditionMarketOnly(true);
        entity.setMarket(newMarket);

        for (String condition : marketConditions)
        {
            newMarket.addCondition(condition);
        }
        return newMarket;
    }










    //it's a LAST string, noone can pass true it!
}