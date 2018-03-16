class Concurrency {
    constructor(capacity){
        this.capacity = capacity;
        this.length = this.capacity;
        this.container = new Array(this.capacity);
        this.queeu = null;
        this.container_promise = null;
    }
    async push(task){
        if(this.length < this.capacity){
            await this.container.push(task);
            this.container_promise = Promise.race(this.container).then(() => {
                // this.container
            });
        }else{
            this.queeu = task;// block push
        }
    }
}