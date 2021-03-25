package org.minions.common.model.kafka;

/**
 * Database Table Remarks:
 *   网易云评论原始数据
 *
 * This class was generated by MyBatis Generator.
 * This class corresponds to the database table music_raw
 */
public class MusicRaw {
    /**
     * Database Column Remarks:
     *   歌曲id
     *
     * This field was generated by MyBatis Generator.
     * This field corresponds to the database column music_raw.song_id
     *
     * @mbg.generated Thu Dec 31 00:41:22 CST 2020
     */
    private String songId;

    /**
     * Database Column Remarks:
     *   歌曲评论原始数据
     *
     * This field was generated by MyBatis Generator.
     * This field corresponds to the database column music_raw.comments
     *
     * @mbg.generated Thu Dec 31 00:41:22 CST 2020
     */
    private String comments;

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table music_raw
     *
     * @mbg.generated Thu Dec 31 00:41:22 CST 2020
     */
    public MusicRaw(String songId, String comments) {
        this.songId = songId;
        this.comments = comments;
    }

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table music_raw
     *
     * @mbg.generated Thu Dec 31 00:41:22 CST 2020
     */
    public MusicRaw() {
        super();
    }

    /**
     * This method was generated by MyBatis Generator.
     * This method returns the value of the database column music_raw.song_id
     *
     * @return the value of music_raw.song_id
     *
     * @mbg.generated Thu Dec 31 00:41:22 CST 2020
     */
    public String getSongId() {
        return songId;
    }

    /**
     * This method was generated by MyBatis Generator.
     * This method sets the value of the database column music_raw.song_id
     *
     * @param songId the value for music_raw.song_id
     *
     * @mbg.generated Thu Dec 31 00:41:22 CST 2020
     */
    public void setSongId(String songId) {
        this.songId = songId == null ? null : songId.trim();
    }

    /**
     * This method was generated by MyBatis Generator.
     * This method returns the value of the database column music_raw.comments
     *
     * @return the value of music_raw.comments
     *
     * @mbg.generated Thu Dec 31 00:41:22 CST 2020
     */
    public String getComments() {
        return comments;
    }

    /**
     * This method was generated by MyBatis Generator.
     * This method sets the value of the database column music_raw.comments
     *
     * @param comments the value for music_raw.comments
     *
     * @mbg.generated Thu Dec 31 00:41:22 CST 2020
     */
    public void setComments(String comments) {
        this.comments = comments == null ? null : comments.trim();
    }
}