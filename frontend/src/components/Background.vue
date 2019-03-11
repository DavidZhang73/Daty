<template>
	<div class="background-wrap" :style="backgroundStyle">
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
                    background: "no-repeat top/100% url(" + require("../assets/img/" + this.imgName) + ")",
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
	.background-wrap {
		position fixed
		width 100%
		height 100%
		transform translate(0, 60px)
	}
</style>
