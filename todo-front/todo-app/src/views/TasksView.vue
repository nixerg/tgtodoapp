<template>
    <div class="tasks-container">
        <div class="tasks-header">
            <input v-model="newTask" type="text" placeholder="Enter task" 
                class="task-input" @keyup.enter="createTask" />
            <button @click="createTask" class="add-button">+</button>
        </div>

        <div class="tasks-list">
            <div v-for="task in tasks" :key="task.id" class="task-item">
                <div class="task-text"> {{task.title}} </div>
                <button class="complete-button" @click="completeTask(task.id)">Done</button>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "TaskView",
        data() {
            return {
                tasks: [], newTask: ""}
        },
        async mounted() {
            await this.fetchTasks();
        },
        methods: {
            async fetchTasks() {
                try {
                    const tg_user = window.Telegram.WebApp.initDataUnsafe?.user
                    const response = await fetch(`https://miniature-spoon-grxg7qwjw79fv6v4-8000.app.github.dev/api/tasks/${tg_user.id}`);
                    const data = await response.json();
                    this.tasks = data;
                } catch (error) {
                    console.error("Error fetching tasks:", error);
                }
            },
            async createTask() {
                if (!this.newTask) return
                try {
                    const tg_user = window.Telegram.WebApp.initDataUnsafe?.user
                    const response = await fetch(`https://miniature-spoon-grxg7qwjw79fv6v4-8000.app.github.dev/api/add`, {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({
                            tg_id: tg_user.id,
                            title: this.newTask
                        })
                    });
                    if (response.ok) {
                        this.newTask = "";
                        await this.fetchTasks();
                    } else {
                        console.error("Error creating task:", response.statusText);
                    }
                } catch (error) {
                    console.error("Error fetching tasks:", error);
                }
            },
            async completeTask(taskId) {
                try {
                    const response = await fetch(`https://miniature-spoon-grxg7qwjw79fv6v4-8000.app.github.dev/api/completed`, {
                        method: "PATCH",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({ id: taskId })
                    });
                    if (response.ok) {
                        await this.fetchTasks();
                    } else {
                        console.error("Error completing task:", response.statusText);
                    }
                } catch (error) {
                    console.error("Error fetching tasks:", error);
                }
            }
        }
    }
</script>            

<style scoped>

.tasks-container {
    flex: 1;
    display: flex;
    flex-direction: column;
    overflow-y: auto;
    padding: 16px;
}

.task-header {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    margin-bottom: 16px;
}

.task-input {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 16px;
}

.add-button {
    background-color: #4CAF50;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
}

.tasks-list {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.task-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    margin-bottom: 10px;
}

.task-text {
    font-size: 16px;
}

.complete-button {
    background-color: #4CAF50;
    color: white;
    border: none;
    padding: 5px 10px;
    border-radius: 5px;
    cursor: pointer;
}
</style>