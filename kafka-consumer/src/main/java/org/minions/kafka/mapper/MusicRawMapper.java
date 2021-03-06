package org.minions.kafka.mapper;

import org.apache.ibatis.annotations.Param;
import org.minions.common.model.kafka.MusicRaw;
import org.minions.common.model.kafka.MusicRawExample;

import java.util.List;

public interface MusicRawMapper {
    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table music_raw
     *
     * @mbg.generated Thu Dec 31 00:41:22 CST 2020
     */
    long countByExample(MusicRawExample example);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table music_raw
     *
     * @mbg.generated Thu Dec 31 00:41:22 CST 2020
     */
    int deleteByExample(MusicRawExample example);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table music_raw
     *
     * @mbg.generated Thu Dec 31 00:41:22 CST 2020
     */
    int deleteByPrimaryKey(String songId);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table music_raw
     *
     * @mbg.generated Thu Dec 31 00:41:22 CST 2020
     */
    int insert(MusicRaw record);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table music_raw
     *
     * @mbg.generated Thu Dec 31 00:41:22 CST 2020
     */
    int insertSelective(MusicRaw record);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table music_raw
     *
     * @mbg.generated Thu Dec 31 00:41:22 CST 2020
     */
    List<MusicRaw> selectByExample(MusicRawExample example);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table music_raw
     *
     * @mbg.generated Thu Dec 31 00:41:22 CST 2020
     */
    MusicRaw selectByPrimaryKey(String songId);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table music_raw
     *
     * @mbg.generated Thu Dec 31 00:41:22 CST 2020
     */
    int updateByExampleSelective(@Param("record") MusicRaw record, @Param("example") MusicRawExample example);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table music_raw
     *
     * @mbg.generated Thu Dec 31 00:41:22 CST 2020
     */
    int updateByExample(@Param("record") MusicRaw record, @Param("example") MusicRawExample example);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table music_raw
     *
     * @mbg.generated Thu Dec 31 00:41:22 CST 2020
     */
    int updateByPrimaryKeySelective(MusicRaw record);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table music_raw
     *
     * @mbg.generated Thu Dec 31 00:41:22 CST 2020
     */
    int updateByPrimaryKey(MusicRaw record);
}