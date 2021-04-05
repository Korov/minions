package org.minions.common.utils

class CollectionUtil {
    companion object {
        fun isEmpty(collections: Collection<*>?): Boolean {
            return collections == null || collections.isEmpty()
        }
    }
}