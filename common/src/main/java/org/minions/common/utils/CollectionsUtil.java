package org.minions.common.utils;

import java.util.Collection;

public class CollectionsUtil {
    public static boolean isEmpty(Collection collections) {
        if (null == collections || 0 == collections.size()) {
            return false;
        }
        return true;
    }
}
