<template>
	<div class="home-wrap">
<!--		<Background img-name="background.jpg"-->
<!--		            :blur="false"></Background>-->
		<div class="home">
			<img class="logo" src="../assets/home_logo.svg" alt="LOGO">
			<div class="button-row">
				<router-link :to="{name: 'addNewCollection'}">
					<el-button type="primary">
						<i class="el-icon-download"></i>
						我要收文件
					</el-button>
				</router-link>
				<router-link :to="{name: 'collectionList'}">
					<el-button type="primary" id="last-btn">
						<i class="el-icon-upload2"></i>
						我要交文件
					</el-button>
				</router-link>
			</div>
		</div>
	</div>
</template>

<script>
    import Background from '../components/Background'

    export default {
        name: 'home',
        components: {
            Background
        }
    }
</script>

<style lang="stylus">
	.home-wrap {
		background-size: contain

		.home {
			padding-top 25vh
			margin 0 auto
			width 35vw

			.logo {
				width 100%
			}

			.button-row {
				margin 5vh auto
				padding 0 3vw

				button {
					font-size 16px
				}

				#last-btn {
					float right

					&::after {
						content ''
						display block
						clear both
					}
				}
			}
		}
	}

	@media (max-width: 1024px) {
		.home-wrap {
			.home {
				width 85vw
			}
		}
	}
</style>
