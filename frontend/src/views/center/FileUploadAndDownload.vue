<template>
    <div class="fileUploadAndDownload-wrap">
        <el-row v-loading="Loading"
                element-loading-text="拼命加载中"
                element-loading-spinner="el-icon-loading"
                element-loading-background="rgba(255, 255, 255, 1)">
            <el-col :xs="{span:24}"
                    :sm="{span:24}"
                    :lg="{span:24}">
                <div class="title" align="center">
                    <h1 class="text">{{collectionInfo.name}}</h1>
                    <h6>创建人：{{creator.username}}</h6>
                </div>
                <el-divider content-position="left">起止时间</el-divider>
                <p class="time">提交开始时间：{{collectionInfo.start_datetime}}</p>
                <p class="time">提交截至时间：{{collectionInfo.end_datetime}}</p>
                <el-divider content-position="left">文件要求</el-divider>
                <p class="require">{{collectionInfo.description || '无'}}</p>
                <el-divider content-position="left">模板文件</el-divider>
                <div v-if="template_file" class="template-file">
                    <span>
                        <el-button
                                type="primary"
                                size="mini"
                                plain
                                @click="downloadSingleFile(collectionInfo.template_file)">下载
                        </el-button>
                    </span>
                    <span class="file-name">{{template_file.name}}</span>
                </div>
                <div v-else class="template-file">无</div>
                <el-collapse v-model="activeNames" accordion>
                    <el-collapse-item v-for="fileInfo in fileList" :name="fileInfo.id">
                        <template slot="title">
                            {{fileInfo.uploader.name}}
                            <el-tag
                                    v-if="fileInfo.file"
                                    size="mini"
                                    type="success"
                                    effect="light">已提交
                            </el-tag>
                            <el-tag v-else
                                    size="mini"
                                    type="danger"
                                    effect="light">未提交
                            </el-tag>
                        </template>
                        <el-upload
                                :action="action"
                                :before-upload="beforeUploadCheck"
                                :on-error="uploadErr"
                                :on-success="uploadSuc"
                                :before-remove="beforeRemove"
                                :headers="headers"
                                :limit="1">
                            <el-popover
                                    placement="top-start"
                                    title="注意！"
                                    width="200"
                                    trigger="hover"
                                    content="文件大小不得超过10MB,每个文件集只能存在一个模板文件,请删除原文件后再上传">
                                <el-button
                                        size="small"
                                        type="primary"
                                        plain
                                        slot="reference">点击上传
                                </el-button>
                            </el-popover>
                        </el-upload>
                        <el-button
                                v-if="$store.state.user && $store.state.user.id === creator.id"
                                class="downloadBtn"
                                size="small"
                                type="info"
                                @click="downloadSingleFile(fileInfo.file)"
                                plain>下载文件
                        </el-button>
                    </el-collapse-item>
                </el-collapse>
                <div class="btnGroup" v-if="$store.state.user && $store.state.user.id === creator.id">
                    <el-button
                            class="downloadAll"
                            type="primary"
                            @click="downloadAllFiles">下载全部
                    </el-button>
                    <el-button
                            class="shareCollection"
                            type="info"
                            v-clipboard:copy="url"
                            v-clipboard:success="onCopy"
                            v-clipboard:error="onError">复制分享链接
                    </el-button>
                </div>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    import api from '../../api'

    export default {
        name: "fileUploadAndDownload",
        data() {
            return {
                params: {},
                headers: {},
                Loading: true,
                action: '/api/file/',
                collectionInfo: {},
                creator: {},
                template_file: {},
                activeNames: '',
                fileList: [],
                url: window.location.href,
            }
        },
        mounted() {
            this.getCollectionInfo();
            this.getHeaders();
        },
        methods: {
            getHeaders() {
                this.headers['X-CSRFToken'] = this.getCookie('csrftoken');
                this.headers['credentials'] = 'include';
            },
            getCollectionInfo() {
                this.Loading = true;
                api.getCollectionById(this.$route.params.id).then(data => {
                    this.collectionInfo = data;
                    this.creator = data.creator;
                    this.template_file = data.template_file;
                    this.params['collection_id'] = this.$route.params.id;
                    api.getFileListById(this.params).then(data => {
                        console.log(data);
                        this.fileList = data;
                        this.Loading = false;
                    });
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
            uploadSuc(response, file) {
                api.uploadFileById(this.activeNames, response.id);
                this.collectionInfo = {};
                this.creator = {};
                this.template_file = {};
                this.fileList = [];
                this.getCollectionInfo();
            },
            beforeRemove(file) {
                return this.$confirm(`确定移除 ${file.name}？`);
            },
            downloadSingleFile(file) {
                let tempFileObj = {};
                tempFileObj = file;
                if (tempFileObj) {
                    window.open(tempFileObj.file);
                } else {
                    this.$message({
                        showClose: true,
                        type: 'error',
                        message: '该用户没有提交文件'
                    });
                }
            },
            downloadAllFiles() {
                window.open('/api/collection/file/all/?collection_id=' + this.$route.params.id);
            },
            onCopy() {
                this.$message({
                    showClose: true,
                    type: 'success',
                    message: '链接已复制到剪切板'
                });
            },
            onError() {
                this.$message({
                    showClose: true,
                    type: 'error',
                    message: '复制失败，请重试'
                });
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
    .fileUploadAndDownload-wrap {
        width 100%

        .title {

            .text {
                margin 10px 0 10px 0
            }
        }

        .time {
            margin 5px 20px 0 20px
        }

        .require {
            margin 5px 20px 20px 20px
        }

        .template-file {
            margin 5px 20px 20px 20px

            .file-name {
                margin-left 20px
            }
        }

        .el-collapse {
            width 100%

            .el-collapse-item {
                width 100%

                .el-tag {
                    margin-left 10px
                }

                .el-upload {
                    margin 10px 10px 0 10px
                }

                .downloadBtn {
                    margin 10px 10px 0 10px
                }
            }
        }

        .btnGroup {
            margin-top 10px
            float right
            right 0
        }
    }
</style>