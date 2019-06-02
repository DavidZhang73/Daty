<template>
    <div class="editCollection-wrap">
        <el-row v-loading="formLoading"
                element-loading-text="拼命加载中"
                element-loading-spinner="el-icon-loading"
                element-loading-background="rgba(255, 255, 255, 1)">
            <el-col :lg="{span: 18}"
                    :sm="{span: 20}"
                    :xs="{span: 24}">
                <el-form
                        class="editCollection-form"
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
                                  v-model.trim="collectionForm.description">
                        </el-input>
                    </el-form-item>
                    <el-form-item label="用户组" prop="usergroup">
                        <div style="text-align: left">
                            <el-transfer
                                    style="text-align: left; display: inline-block"
                                    v-model="collectionForm.usergroup"
                                    filterable
                                    :titles="['已有用户组', '已选中用户组']"
                                    :button-texts="['删除', '添加']"
                                    :format="{noChecked: '${total}',hasChecked: '${checked}/${total}'}"
                                    :data="userGroups">
                            </el-transfer>
                        </div>
                    </el-form-item>
                    <el-form-item label="提交起止日期" prop="start_datetime">
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
                    <el-form-item label="模板文件" prop="fileUUID">
                        <el-upload
                                class="upload"
                                drag
                                :action="action"
                                :before-upload="beforeUploadCheck"
                                :on-error="uploadErr"
                                :on-remove="uploadRemove"
                                :on-success="uploadSuc"
                                :before-remove="beforeRemove"
                                :file-list="fileList"
                                :limit="1">
                            <i class="el-icon-upload"></i>
                            <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
                            <div class="el-upload__tip" slot="tip">文件大小不得超过10MB,每个文件集只能存在一个模板文件,请删除原文件后再上传</div>
                        </el-upload>
                    </el-form-item>
                    <el-form-item>
                        <div class="btnGroup">
                            <el-button
                                    type="primary"
                                    class="submitBtn"
                                    @click="submitCollectionForm('collectionForm')">提交
                            </el-button>
                            <el-button
                                    type="danger"
                                    class="deleteBtn"
                                    @click="deleteCollectionForm">删除
                            </el-button>
                        </div>
                    </el-form-item>
                </el-form>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    import api from '../../api'

    export default {
        name: "EditCollection",
        data() {
            var validateName = (rule, value, callback) => {
                if (!value) {
                    return callback(new Error('文件集名称不可为空'))
                } else if (value.length > 128) {
                    return callback(new Error('文件集名称应该小于128个字符'))
                }
                return callback()
            };
            var validateFileRequire = (rule, value, callback) => {
                if (value.length > 300) {
                    return callback(new Error('文件要求应该小于300个字符'))
                }
                return callback()
            };
            var validateUserGroups = (rule, value, callback) => {
                if (value.length === 0) {
                    return callback(new Error('用户组不能为空'))
                }
                return callback()
            };
            var validateTime = (rule, value, callback) => {
                if (!value) {
                    return callback(new Error('起止日期不可为空'))
                }
                return callback()
            };
            return {
                formLoading: true,
                collectionForm: {},
                collectionFormRules: {
                    name: [
                        {validator: validateName, trigger: 'blur'}
                    ],
                    description: [
                        {validator: validateFileRequire, trigger: 'blur'}
                    ],
                    usergroup: [
                        {validator: validateUserGroups, trigger: 'blur'}
                    ],
                    start_datetime: [
                        {validator: validateTime, trigger: 'blur'}
                    ]
                },
                timeList: [],
                fileList: [],
                userGroups: [],
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
                action: 'https://jsonplaceholder.typicode.com/posts/',
            }
        },
        mounted() {
            //api
            this.getCollectionInfo();
        },
        methods: {
            getCollectionInfo() {
                this.formLoading = true;
                api.getOrUpdateAllUserGroups().then(data => {
                    for (var i = 0; i < data.results.length; i++) {
                        let temp = {};
                        temp.key = data.results[i].id;
                        temp.label = data.results[i].name;
                        this.userGroups.push(temp);
                    }
                });
                api.getCollectionListById(this.$route.params.id).then(data => {
                    this.collectionForm = data;
                    //Time
                    let timeBegin = new Date(data.start_datetime);
                    let timeEnd = new Date(data.end_datetime);
                    this.timeList.push(timeBegin);
                    this.timeList.push(timeEnd);
                    this.formLoading = false;
                });
            },
            beforeUploadCheck(file) {
                let isLt10M = file.size / 1024 / 1024 < 10;
                if (!isLt10M) {
                    this.$message.error('上传失败，文件大小超过10MB !');
                }
                return isLt10M;
            },
            uploadErr() {
                this.$message.error('上传失败，请尝试重新上传 !');
            },
            uploadRemove() {
                this.fileList.pop();
                //TODO
            },
            uploadSuc(response, file) {
                this.collectionForm.template_file = JSON.parse(JSON.stringify(file.uid));
                let fileObj = {};
                fileObj.name = file.name;
                fileObj.uid = file.uid;
                this.fileList.push(fileObj);
                console.log(this.fileList);
            },
            beforeRemove(file) {
                return this.$confirm(`确定移除 ${file.name}？`);
            },
            submitCollectionForm(formName) {
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        this.formLoading = true;
                        api.updateCollectionById(
                            this.$route.params.id,
                            this.collectionForm.name,
                            this.$store.state.user.id,
                            this.collectionForm.description,
                            this.collectionForm.start_datetime,
                            this.collectionForm.end_datetime,
                            this.collectionForm.template_file,
                            this.collectionForm.usergroup
                        ).then(data => {
                            if (data.error) {
                                this.formLoading = false;
                                this.$message.error({showClose: true, message: data.error});
                            } else {
                                this.formLoading = false;
                                this.$router.push({name: 'collectionList'});
                            }
                        })
                    } else return false;
                })
            },
            deleteCollectionForm() {
                this.$confirm('此操作将永久删除该文件集, 是否继续?', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    //api
                    this.formLoading = true;
                    api.deleteCollectionById(this.$route.params.id);
                    this.formLoading = false;
                    this.$router.push({name: 'collectionList'});
                    this.$message({
                        type: 'success',
                        message: '删除成功!'
                    });
                }).catch(() => {
                    this.$message({
                        type: 'info',
                        message: '已取消删除'
                    });
                });
            }
        },
        watch: {
            timeList(newVal) {
                if (newVal) {
                    this.collectionForm.start_datetime = newVal[0];
                    this.collectionForm.end_datetime = newVal[1];
                }
            }
        }
    }
</script>

<style lang="stylus">
    .editCollection-wrap {
        width 100%

        .editCollection-form {
            width 100%

            .el-form-item {
                width 100%

                .btnGroup {
                    float right
                    right 0
                }
            }
        }
    }
</style>