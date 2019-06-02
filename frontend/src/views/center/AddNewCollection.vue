<template>
    <div class="addNewCollection-wrap">
        <el-row v-loading="formLoading"
                element-loading-text="拼命加载中"
                element-loading-spinner="el-icon-loading"
                element-loading-background="rgba(255, 255, 255, 1)">
            <el-col :lg="{span: 18}"
                    :sm="{span: 20}"
                    :xs="{span: 24}"
                    style="text-align: left">
                <el-form class="addNewCollection-form"
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
                        <div>
                            <el-transfer
                                    style="text-align: left; display: inline-block"
                                    v-model="collectionForm.userGroup"
                                    filterable
                                    :titles="['已有用户组', '已选中用户组']"
                                    :button-texts="['删除', '添加']"
                                    :format="{noChecked: '${total}',hasChecked: '${checked}/${total}'}"
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
                    <el-form-item label="模板文件" prop="fileUUID">
                        <el-upload
                                class="upload"
                                drag
                                :action="action"
                                :before-upload="beforeUploadCheck"
                                :on-error="uploadErr"
                                :on-success="uploadSuc"
                                :headers="headers"
                                :limit="1">
                            <i class="el-icon-upload"></i>
                            <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
                            <div class="el-upload__tip" slot="tip">文文件大小不得超过10MB,每个文件集只能存在一个模板文件,请删除原文件后再上传</div>
                        </el-upload>
                    </el-form-item>
                    <el-form-item>
                        <el-button
                                type="primary"
                                class="submitBtn"
                                @click="submitCollectionForm('collectionForm')">提交
                        </el-button>
                    </el-form-item>
                </el-form>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    import api from '../../api'

    export default {
        name: "AddNewCollection",
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
                if (value.length === 0) {
                    return callback(new Error('起止日期不可为空'))
                }
                return callback()
            };
            return {
                formLoading: true,
                collectionForm: {
                    name: '',
                    fileRequire: '',
                    time: [],
                    timeBegin: '',
                    timeEnd: '',
                    fileId: '',
                    userGroup: [],
                },
                timeList: [],
                collectionFormRules: {
                    name: [
                        {validator: validateName, trigger: 'blur'}
                    ],
                    fileRequire: [
                        {validator: validateFileRequire, trigger: 'blur'}
                    ],
                    userGroup: [
                        {validator: validateUserGroups, trigger: 'blur'}
                    ],
                    time: [
                        {validator: validateTime, trigger: 'blur'}
                    ]
                },
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
                action: '/api/file/',
                headers: {},
            }
        },
        watch: {
            timeList(newVal) {
                this.collectionForm.time = JSON.parse(JSON.stringify(newVal));
                this.collectionForm.timeBegin = JSON.parse(JSON.stringify(newVal[0]));
                this.collectionForm.timeEnd = JSON.parse(JSON.stringify(newVal[1]));
            }
        },
        mounted() {
            this.getOrUpdateGroupInfo();
            this.getHeaders();
        },
        methods: {
            getHeaders() {
                this.headers['X-CSRFToken'] = this.getCookie('csrftoken');
                this.headers['credentials'] = 'include';
            },
            getOrUpdateGroupInfo() {
                this.formLoading = true;
                api.getOrUpdateAllUserGroups().then(data => {
                    for (var i = 0; i < data.results.length; i++) {
                        let temp = {};
                        temp.key = data.results[i].id;
                        temp.label = data.results[i].name;
                        this.userGroups.push(temp);
                    }
                    this.formLoading = false;
                })
            },
            beforeUploadCheck(file) {
                const isLt10M = file.size / 1024 / 1024 < 10;
                if (!isLt10M) {
                    this.$message.error('上传失败，文件大小超过10MB !');
                }
                return isLt10M
            },
            uploadErr(err, file) {
                this.$message.error('上传失败，请尝试重新上传 !');
            },
            uploadSuc(response, file) {
                this.collectionForm.fileId = response.id;
            },
            submitCollectionForm(formName) {
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        this.formLoading = true;
                        api.updateCollection(
                            this.$store.state.user.id,
                            this.collectionForm.name,
                            this.collectionForm.fileRequire,
                            this.collectionForm.timeBegin,
                            this.collectionForm.timeEnd,
                            this.collectionForm.fileId,
                            this.collectionForm.userGroup
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
            getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie !== '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = cookies[i].trim();
                        if (cookie.substring(0, name.length + 1) === (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }
        }
    }
</script>

<style lang="stylus">
    .addNewCollection-wrap {
        width 100%

        .addNewCollection-form {
            width 100%

            .el-form-item {
                width 100%

                .submitBtn {
                    float right
                    right 0
                }
            }
        }
    }
</style>