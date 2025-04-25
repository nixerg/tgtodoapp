<template>
    <div class="profile-container">
        <h2>Profile</h2>
        <div class="profile-info">
            <p>ID: {{ user.id }}</p>
            <p>Name: {{ user.name }}</p>
            <p>Tasks: {{ user.completeTask }}</p>
        </div>
        <div><p>Version: {{ version }}</p></div>
        <!--<button class="test-button" @click="DoTest()">Test</button>-->
    </div>
</template>

<script>
export default {
    name: 'ProfileView',
    data() {
        return {
            user: {
                id: '',
                name: '',
                completeTask: 0,
            },
            version: '',
        }
    },
    async mounted() {
        await this.fetchProfile();
        await this.fetchVersion();
    },
    methods: {
        async fetchProfile() {
            try {
                const tg_user = window.Telegram.WebApp.initDataUnsafe?.user
                const response = await fetch(`https://miniature-spoon-grxg7qwjw79fv6v4-8000.app.github.dev/api/main/${tg_user.id}`);
                const data = await response.json();
                this.user.id = tg_user.id;
                this.user.name = tg_user.first_name;
                this.user.completeTask = data.completedTasks;
            } catch (error) {
                console.error("Error fetching profile:", error);
            }
        },
        async fetchVersion() {
            try {
                const response = await fetch(`https://miniature-spoon-grxg7qwjw79fv6v4-8000.app.github.dev/api/version`);
                const data = await response.json();
                this.version = data.version;
            } catch (error) {
                console.error("Error fetching version:", error);
            }
        },
        //async DoTest() {
        //    try {
        //        const response = await fetch(`https://miniature-spoon-grxg7qwjw79fv6v4-8000.app.github.dev/test`);
        //        const data = await response.json();
        //        console.log(data);
        //    } catch (error) {
        //        console.error("Error fetching profile:", error);
        //    }
        //},
    }
}
</script>

<style scoped>
.profile-container {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 16px;
}
.profile-info {
    background-color: antiquewhite;
    backdrop-filter: blur(8px);
    padding: 16px;
    border-radius: 8px;
    text-align: center;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    margin-top: 16px;
    width: 100%;
    max-width: 320px;
}
</style>