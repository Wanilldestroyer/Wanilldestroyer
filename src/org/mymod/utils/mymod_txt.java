package org.niatahl.scalartech.utils;

import com.fs.starfarer.api.Global;

public class mymod_txt {
    private static final String scalartech="scalartech";
    public static String txt(String id){
        return Global.getSettings().getString(scalartech, id);
    }    
}