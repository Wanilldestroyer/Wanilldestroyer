package jars.org.mymod.world;

import com.fs.starfarer.api.campaign.FactionAPI;
import com.fs.starfarer.api.campaign.SectorAPI;
import com.fs.starfarer.api.campaign.SectorGeneratorPlugin;


public class ScalarRelationPlugin implements SectorGeneratorPlugin {

    //Just call initFactionRelationships: this is only intended as a means to set faction relations at start
    @Override
    public void generate(SectorAPI sector) {
        initFactionRelationships(sector);
    }

    public static void initFactionRelationships(SectorAPI sector) {
        FactionAPI RedDragon = sector.getFaction("RedDragon");

        //but not pirates and dabble
        scalartech.setRelationship("pirates",-0.6f);
    }