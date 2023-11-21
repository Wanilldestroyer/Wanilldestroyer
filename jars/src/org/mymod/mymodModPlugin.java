package jars.src.org.mymod;

import com.fs.starfarer.api.BaseModPlugin;
import com.fs.starfarer.api.Global;

public class mymodModPlugin extends BaseModPlugin {
    private static void initMyMod() {
        new MyModGen().generate(Global.getSector());
    }

    @Override
    public void onNewGame() {
        Global.getLogger(this.getClass()).info("Hooray i finally edit mods!");
        initMyMod();
    }
}