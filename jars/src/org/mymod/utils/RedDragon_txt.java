package jars.src.org.mymod.utils;

import com.fs.starfarer.api.Global;

public class RedDragon_txt {
    private static final String RedDragon="RedDragon";
    public static String txt(String id){
        return Global.getSettings().getString(RedDragon, id);
    }
}