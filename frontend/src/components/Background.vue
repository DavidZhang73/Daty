<template>
	<div class="user-background-wrap" :style="backgroundStyle">

	</div>
</template>

<script>
    export default {
        name: "UserBackground",
        props: {
            imgName: String,
            blur: Boolean,
        },
        data() {
            return {
                backgroundStyle: {
                    background: "no-repeat center/100% url(" + require("../assets/img/" + this.imgName) + ")",
                    filter: this.blurStyle(),
                }
            }
        },
        methods: {
            blurStyle() {
                if (this.blur) {
                    return 'blur(3px)'
                } else {
                    return 'blur(0px)'
                }

            }
        }
    }
</script>

<style lang="stylus">
	.user-background-wrap {
		position absolute
		width 100%
		height 100%
	}
</style>
