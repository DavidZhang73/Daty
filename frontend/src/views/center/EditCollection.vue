<template>
    <div class="EditCollection-wrap">
        <el-row
                v-loading="false"
                element-loading-text="拼命加载中"
                element-loading-spinner="el-icon-loading"
                element-loading-background="rgba(255, 255, 255, 1)">
            <el-col :lg="{span: 18}"
                    :sm="{span: 20}"
                    :xs="{span: 24}">
                <el-form
                        class="EditCollection-form"
                        :model="collectionForm"
                        ref="collectionForm"
                        label-position="left"
                        label-width="100px"
                        :rules="collectionFormRules"
                        status-icon>
                    <el-form-item label="文件集名称" prop="name">
                        <el-input v-model.trim="collectionForm.name" placeholder="请输入文件集名称"></el-input>
                    </el-form-item>
                    <el-form-item label="文件要求" prop="fileRequire">
                        <el-input type="textarea"
                                  :autosize="{ minRows: 3, maxRows: 6}"
                                  placeholder="请输入文件要求"
                                  v-model.trim="collectionForm.fileRequire">
                        </el-input>
                    </el-form-item>
                    <el-form-item label="用户组" prop="userGroup">
                        <div style="text-align: left">
                            <el-transfer
                                    style="text-align: left; display: inline-block"
                                    v-model="collectionForm.userGroup"
                                    filterable
                                    :titles="['已有用户组', '已选中用户组']"
                                    :button-texts="['删除', '添加']"
                                    :format="{noChecked: '${total}',hasChecked: '${checked}/${total}'}"
                                    @change="transferHandleChange"
                                    :data="userGroups">
                            </el-transfer>
                        </div>
                    </el-form-item>
                    <el-form-item label="提交起止日期" prop="time">
                        <el-date-picker v-model="timeList"
                                        type="datetimerange"
                                        align="right"
                                        :picker-options="pickerOptions"
                                        range-separator="至"
                                        start-placeholder="开始日期"
                                        end-placeholder="结束日期"
                                        value-format="yyyy-MM-dd hh:mm:ss">
                        </el-date-picker>
                    </el-form-item>
                </el-form>
            </el-col>
        </el-row>
    </div>
</template>

<script>

    export default {
        name: "EditCollection",
        data() {
            return {
                formLoading: true,
                collectionForm: {
                    name: 'test',
                    fileRequire: 'testRe',
                    time: [],
                    timeBegin: '2019-04-29 11:49:39',
                    timeEnd: '2019-05-29 11:49:39',
                    fileUUID: '',
                    userGroup: [1, 4],
                },
                collectionFormRules: {},
                timeList: [],
                userGroups: [
                    {
                        key: 1,
                        label: 'aaa'
                    },
                    {
                        key: 2,
                        label: 'bbb'
                    },
                    {
                        key: 3,
                        label: 'ccc'
                    },
                    {
                        key: 4,
                        label: 'ddd'
                    }
                ],
                pickerOptions: {
                    shortcuts: [{
                        text: '最近一周',
                        onClick(picker) {
                            const end = new Date();
                            const start = new Date();
                            start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
                            picker.$emit('pick', [start, end]);
                        }
                    }, {
                        text: '最近一个月',
                        onClick(picker) {
                            const end = new Date();
                            const start = new Date();
                            start.setTime(start.getTime() - 3600 * 1000 * 24 * 30);
                            picker.$emit('pick', [start, end]);
                        }
                    }, {
                        text: '最近三个月',
                        onClick(picker) {
                            const end = new Date();
                            const start = new Date();
                            start.setTime(start.getTime() - 3600 * 1000 * 24 * 90);
                            picker.$emit('pick', [start, end]);
                        }
                    }]
                },
            }
        },
        mounted() {
            let timeBeginFormatYY = this.collectionForm.timeBegin.substring(0, 4);
            let timeBeginFormatMM = this.collectionForm.timeBegin.substring(5, 7);
            let timeBeginFormatDD = this.collectionForm.timeBegin.substring(8, 10);
            let timeBeginFormatHH = this.collectionForm.timeBegin.substring(11, 13);
            let timeBeginFormatMin = this.collectionForm.timeBegin.substring(14, 16);
            let timeBeginFormatSS = this.collectionForm.timeBegin.substring(17, 19);

            let timeEndFormatYY = this.collectionForm.timeBegin.substring(0, 4);
            let timeEndFormatMM = this.collectionForm.timeBegin.substring(5, 7);
            let timeEndFormatDD = this.collectionForm.timeBegin.substring(8, 10);
            let timeEndFormatHH = this.collectionForm.timeBegin.substring(11, 13);
            let timeEndFormatMin = this.collectionForm.timeBegin.substring(14, 16);
            let timeEndFormatSS = this.collectionForm.timeBegin.substring(17, 19);

            this.timeList.push(new Date(timeBeginFormatYY, timeBeginFormatMM, timeBeginFormatDD, timeBeginFormatHH, timeBeginFormatMin, timeBeginFormatSS));
            this.timeList.push(new Date(timeEndFormatYY, timeEndFormatMM, timeEndFormatDD, timeEndFormatHH, timeEndFormatMin, timeEndFormatSS));
        },
        methods: {
            transferHandleChange() {
                //TODO
            },
        },
    }
</script>

<style lang="stylus">

</style>