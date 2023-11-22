package org.mymod;
  
public class mymodModPlugin extends BaseModPlugin {
  
  
    //New game stuff
    @Override
    public void onNewGame() {
        SectorAPI sector = Global.getSector();

        //If we have Nexerelin and random worlds enabled, don't spawn our manual systems
        boolean haveNexerelin = Global.getSettings().getModManager().isModEnabled("nexerelin");
        if (!haveNexerelin || SectorManager.getManager().isCorvusMode()){
            new Spindle().generate(sector);
        }

        ScalarRelationPlugin.initFactionRelationships(sector);

        //Adding ScalarTech to bounty system
        SharedData.getData().getPersonBountyEventData().addParticipatingFaction("mymod");

    }

    @Override
    public void onNewGameAfterProcGen() {
    }

    // this should be Edited as F

}