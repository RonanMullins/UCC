let canvas;
let context;

let request_id;

let xhttp;

let fpsInterval = 1000 / 30; //the denominator is frames-per-second
let now;
let then = Date.now();

let blobs = [];
let skeletons = [];
let items = [];
let trees = [];
let decoration = [];

let blobsLimit = 5;
let itemsLimit = 3;
let treesLimit = 3;
let decorationLimit = 10;
let skeletonLimit = 0;

let time_start = Date.now();
let time_elapsed = 0;

let spaceBar = false;
let arrowLeft = false;
let arrowUp = false;
let arrowRight = false;
let arrowDown = false;

let lookRight = false;
let lookLeft = false;

let player = {
    x : 0,
    y : 0,
    width : 48,
    height : 48,
    frameX : 0,
    frameY : 0,
    xChange : 0,
    yChange : 0,
    score : 0
}

let background = [

    [77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77],
    [77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77],
    [77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77],
    [77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77],
    [77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77],
    [77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77],
    [77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77],
    [2,2,2,2,2,2,2,2,3,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77],
    [8,8,8,8,8,8,8,8,9,77,77,77,77,77,1,2,2,2,2,2,2,2,2,2,2,2,3,77,77,77,77,77],
    [8,8,8,8,8,8,8,8,10,3,77,77,77,77,7,8,8,8,8,8,8,8,8,8,8,8,9,77,77,77,77,77],
    [8,8,8,8,8,8,8,8,8,10,2,2,2,2,11,8,8,8,8,8,8,8,8,8,8,8,10,2,2,2,2,2],
    [14,14,14,14,14,5,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8],
    [77,77,77,77,77,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8],
    [77,77,77,77,77,13,14,14,5,8,8,8,8,8,8,4,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14],
    [77,77,77,77,77,77,77,77,7,8,8,8,8,8,8,9,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77],
    [77,77,77,77,77,77,77,77,13,14,14,14,14,14,14,15,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77],
    [77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77],
    [77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77],
    [77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77],
    [77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77]
];

let overlay = [

    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,6,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,8,-1,-1,-1,-1],
    [-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1, -1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1],
    [-1,8,-1,-1,-1,-1,-1,-1,-1,-1,-1,9,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,11,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,17,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,16,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,18,-1,-1,-1,-1,-1,-1,-1,16,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,17,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,17,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,17,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,19,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,16,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,10,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,9,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,4,-1,-1,-1,-1,-1,8,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
];

let tilesPerRow = 6;
let tileSize = 16;

let overlayTilesPerRow = 4;
let overlayTileSize = 16;

let IMAGES = {player: "static/player.png", blob : "static/blob.png", background: "static/background.png", obstacle : "static/objects.png", item : "static/chest.png", decor : "static/decor.png", skeleton : "static/skeleton.png"};

document.addEventListener("DOMContentLoaded", init, false);

function init() {

    canvas = document.querySelector("canvas");
    context = canvas.getContext("2d");

    player.x = canvas.width / 2;
    player.y = canvas.height / 2;

    window.addEventListener("keydown", activate, false);
    window.addEventListener("keyup", deactivate, false);
    
    // draw();
    load_images(draw);

}

function draw() {

    request_id = window.requestAnimationFrame(draw);

    // Throttle FPS
    let now = Date.now();
    let elapsed = now - then;
    if (elapsed <= fpsInterval){
        return; 
    }
    then = now - (elapsed % fpsInterval);

    // Calculate time elapsed
    let time_elapsed = Date.now();
    time_elapsed = time_elapsed - time_start;
    time_elapsed = time_elapsed / 1000; // to get to seconds
    time_elapsed = Math.round(time_elapsed * 100) / 100; // round the number to 2 decimal places

    // Clear canvas
    context.clearRect(0, 0, canvas.width, canvas.height);

    // Background
    for (let r = 0; r < 20; r +=1){
        for (let c = 0; c < 32; c += 1){
            let tile = background[r][c];
            if (tile >= 0) {
                let titleRow = Math.floor(tile / tilesPerRow);
                let titleCol = Math.floor(tile % tilesPerRow);
                context.drawImage(IMAGES.background, 
                    titleCol * tileSize, titleRow * tileSize, tileSize, tileSize,
                    c * tileSize, r * tileSize, tileSize, tileSize);
            }
        }
    }

    // Overlay
    for (let r = 0; r < 20; r +=1){
        for (let c = 0; c < 32; c += 1){
            let tile = overlay[r][c];
            if (tile >= 0) {
                let titleRow = Math.floor(tile / overlayTilesPerRow);
                let titleCol = Math.floor(tile % overlayTilesPerRow);
                context.drawImage(IMAGES.decor, 
                    titleCol * overlayTileSize, titleRow * overlayTileSize, overlayTileSize, overlayTileSize,
                    c * overlayTileSize, r * overlayTileSize, overlayTileSize, overlayTileSize);
            }
        }
    }

    // Create blob
    if (blobs.length < blobsLimit) {
        let b = {
                x : randint(0, canvas.width),
                y : -30,
                width : 32,
                height : 32,
                frameX : 0,
                frameY : 0,
                size : 15,
                xChange : 0,
                yChange : 0,
                hitboxX : 0,
                hitboxY : 0,
                hitboxWidth : 0,
                hitboxHeight : 0,
                deathX : 0,
                deathY : 0
        };
        blobs.push(b);
    }
    // Create skeleton
    if (skeletons.length < skeletonLimit) {
        let s = {
                x : randint(0, canvas.width),
                y : -30,
                width : 64,
                height : 64,
                frameX : 0,
                frameY : 0,
                size : 15,
                xChange : 0,
                yChange : 0,
                hitboxX : 0,
                hitboxY : 0,
                hitboxWidth : 0,
                hitboxHeight : 0,
                deathX : 0,
                deathY : 0
        };
        skeletons.push(s);
    }

    // Create items
    if (items.length < itemsLimit) {
        let i = {
            x : randint(0, canvas.width),
            y : randint(0, canvas.height),
            width : 16,
            height : 16,
            frameX : 0,
            frameY : 0
        };
        items.push(i);
    }

    // Create trees
    if (trees.length < treesLimit) {
        let t = {
            x : randint(0, canvas.width),
            y : randint(0, canvas.height),
            width : 48,
            height : 72,
            frameX : 0,
            frameY : 0,
            hitboxX : 0,
            hitboxY : 0,
            hitboxWidth : 0,
            hitboxHeight : 0
        }; 
        t.y = t.y - t.height;
        trees.push(t);
    }

    // Draw the player
    context.drawImage(IMAGES.player,
        player.frameX * player.width, player.frameY * player.height, player.width, player.height,
        player.x, player.y, player.width, player.height);

    // Draw the blobs
    for (let b of blobs){

        // Update hitbox based off enemy location
        b.hitboxX = b.x + b.width / 2.8;
        b.hitboxY = b.y + b.height / 2;
        b.hitboxWidth = 8;
        b.hitboxHeight = 8;

        context.drawImage(IMAGES.blob,
            b.frameX * b.width, b.frameY * b.height, b.width, b.height,
            b.x, b.y, b.width, b.height);
    }

    // Draw the skeletons
    for (let s of skeletons){

        
        // Update hitbox based off enemy location
        s.hitboxX = s.x + s.width / 2.3;
        s.hitboxY = s.y + s.height / 1.7;
        s.hitboxWidth = 8;
        s.hitboxHeight = 8;
        
        context.drawImage(IMAGES.skeleton,
            s.frameX * s.width, s.frameY * s.height, s.width, s.height,
            s.x, s.y, s.width, s.height);
    }

    // Draw the items
    for (let i of items){
        context.drawImage(IMAGES.item,
            i.frameX * i.width, i.frameY * i.height, i.width, i.height,
            i.x, i.y, i.width, i.height);
    }

    // Draw the trees
    for (let t of trees){

        // Update hitbox based off obstacle location
        t.hitboxX = t.x + t.width / 3;
        t.hitboxY = t.y + t.height / 1.3;
        t.hitboxWidth = 16;
        t.hitboxHeight = 8;
    
        t.frameX = 0;
        t.frameY = 1;
        context.drawImage(IMAGES.obstacle,
            t.frameX * t.width, t.frameY * t.height, t.width, t.height,
            t.x, t.y, t.width, t.height);
    }

    // Declare hit boxes 
    let meleeBox = {
        x : player.x - (player.width / 8),
        y : player.y + (player.height / 4) - 5,
        width : player.width * 1.2,
        height : player.height,  
    }
    let playerhitBox = {
        x : player.x + (player.width / 3),
        y : player.y + (player.height * 0.5) ,
        width : player.width / 3,
        height : player.height - (player.height / 1.5 ),
    }
    
    // Handle key presses // Update player frames
    if (arrowRight === false && arrowLeft === false && arrowUp === false && arrowDown === false){ //Idle  
        
        player.frameY = 0;
        if (lookRight){
            player.frameY = 0;
            player.frameX = (player.frameX + 1) % 6;
        } else {
            player.frameY = 0;
            player.frameX = player.frameX - 1;
            if (player.frameX < 6) {
                player.frameX = 11;
            }
        }
    } 
    if (arrowUp){
        player.yChange = -5;
        player.frameY = 1;
        player.frameX = (player.frameX + 1) % 6;
        
    } 
    if (arrowDown){
        player.yChange = 5;
        player.frameY = 1;
        player.frameX = (player.frameX + 1) % 6;
        
    } 
    if (arrowLeft){
        player.xChange = -5;
        player.frameY = 1;
        player.frameX = player.frameX - 1;
        if (player.frameX < 6) {
            player.frameX = 11;
        }
        lookLeft = true;
        lookRight = false;
        
    } 
    if (arrowRight){
        player.xChange = 5;
        player.frameY = 1;
        player.frameX = (player.frameX + 1) % 6;
        lookRight = true;
        lookLeft = false;
    }
    if (spaceBar){
        if (lookRight){
            player.frameY = 2;
            player.frameX = (player.frameX + 1) % 3;
        } else {
            player.frameY = 2;
            player.frameX = player.frameX - 1;
            if (player.frameX < 3) {
                player.frameX = 11;
            }
        }    
    }
    // Blob movement
    for (let b of blobs) {
        // Confine enemy
        if (b.x < 0){
            b.x = 0;
        } else if (b.x + b.size >= canvas.width){
            b.x = canvas.width - b.size;
        }
        if (b.y < 0){
            b.y = 0;
        } else if (b.y + b.size >= canvas.height){
            b.y = canvas.height - b.size;
        }
        // Chase // Update enemy frames
        if (b.hitboxX < playerhitBox.x){ // if left move right
            b.x = b.x + 0.6;
            b.frameY = 1;
            b.frameX = (b.frameX + 1) % 6;
        }
        if (b.hitboxX > playerhitBox.x){ // if right move left
            b.x = b.x - 0.6;
            b.frameY = 1;
            b.frameX = (b.frameX + 1) % 6;
        }
        if (b.hitboxY < playerhitBox.y){ // if up move down
            b.y = b.y + 0.6;  
        }
        if (b.hitboxY > playerhitBox.y){ // if down move up
            b.y = b.y - 0.6;
        }
    }
    // Skeleton movement
    for (let s of skeletons) {
        // Confine enemy
        if (s.x < 0){
            s.x = 0;
        } else if (s.x + s.size >= canvas.width){
            s.x = canvas.width - s.size;
        }
        if (s.y < 0){
            s.y = 0;
        } else if (s.y + s.size >= canvas.height){
            s.y = canvas.height - s.size;
        }
        // Chase // Update enemy frames
        if (s.hitboxX < playerhitBox.x){ // if left move right
            s.x = s.x + 0.8;
            s.frameY = 1;
            s.frameX = (s.frameX + 1) % 5;
            if ((player.x + player.width)+ 20 < s.hitboxX ||
                (s.hitboxX + s.hitboxWidth) + 20 < player.x ||
                player.y > (s.hitboxY + s.hitboxHeight) + 20 ||
                s.hitboxY > (player.y + player.height) + 20){
              
                } else{
                    s.frameY = 2;
                    s.frameX = (s.frameX + 1) % 4;
                }
        }
        if (s.hitboxX > playerhitBox.x){ // if right move left
            s.x = s.x - 0.8;
            s.frameY = 1;
            s.frameX = s.frameX - 1;
                    if (s.frameX < 6) {
                        s.frameX = 11;
                    }
            if ((player.x + player.width) + 20 < s.hitboxX ||
                (s.hitboxX + s.hitboxWidth) + 20 < player.x ||
                player.y > (s.hitboxY + s.hitboxHeight) + 20 ||
                s.hitboxY > (player.y + player.height) + 20){
              
                } else{
                    s.frameY = 2;
                    s.frameX = s.frameX - 1;
                    if (s.frameX < 4) {
                        s.frameX = 11;
                    }    
                }
        }
        if (s.hitboxY < playerhitBox.y){ // if up move down
            s.y = s.y + 0.8;  
        }
        if (s.hitboxY > playerhitBox.y){ // if down move up
            s.y = s.y - 0.8;
        } 
    }

    // Update player
    player.x = player.x + player.xChange;
    player.y = player.y + player.yChange;  

    // Physics
    player.xChange = player.xChange * 0.4;
    player.yChange = player.yChange * 0.4;
    
    

    // Collision with blob
    for (let b of blobs) {
        if (player_enemy_collides(playerhitBox, b)){
            stop("Game Over!", player.score, time_elapsed);
            return;
        }
    }
    // Collision with skeleton
    for (let s of skeletons) {
        if (player_skeleton_collides(playerhitBox, s)){
            stop("Game Over!", player.score, time_elapsed);
            return;
        }
    }

    // Collision with item
    for (let i of items) {      
        if (player_item_collides(playerhitBox, i)){
            i.x = randint(i.width, canvas.width - i.width);
            i.y = randint(i.height, canvas.height - i.height);
            player.score = player.score + 50; 
        }
    }

    // Collision with obstacle
    for (let t of trees) {
        if (player_obstacle_collides(playerhitBox, t)){
            if (t.hitboxY > playerhitBox.y){ //player moves down
                player.y = t.hitboxY - (playerhitBox.height * 2.5) - 0.1;
            }
            if (t.hitboxY < playerhitBox.y){ //player up
                player.y = t.hitboxY - playerhitBox.height + 0.1;
            }
        }
    }

    // Melee Collision with blobs
    for (let b of blobs) {
        if (spaceBar){
            if (enemy_melee_collides(meleeBox, b)) {

                // death animation
                b.deathX = b.x;
                b.deathY = b.y
                b.frameY = 4;
                b.frameX = (b.frameX + 1) % 4;
                context.drawImage(IMAGES.blob,
                    b.frameX * b.width, b.frameY * b.height, b.width, b.height,
                    b.deathX, b.deathY, b.width, b.height);

                b.x = randint(-30, canvas.width + 30);
                b.y = randint(-30, canvas.height + 30);
                if ((b.x > 0 && b.x < canvas.width) && (b.y > 0 && b.y < canvas.height)){ // if on the screen
                    
                    // 1 = up. 2 = right. 3 = down. 4 = left.
                    let random_direction = randint(1,4); // used to pick random direction
                    if (random_direction === 1){
                        b.y = b.y - canvas.height;
                    }
                    if (random_direction === 2){
                        b.x = b.x + canvas.width;
                    }
                    if (random_direction === 3){
                        b.y = b.y + canvas.height;
                    }
                    if (random_direction === 4){
                        b.x = b.x - canvas.width;
                    }
                }

                player.score = player.score + 10;
            }
        }
    }
    // Melee Collision with skeletons
    for (let s of skeletons) {
        if (spaceBar){

            if (skeleton_melee_collides(meleeBox, s)) {

                // death animation
                s.deathX = s.x;
                s.deathY = s.y
                s.frameY = 4;
                s.frameX = (s.frameX + 1) % 4;
                context.drawImage(IMAGES.skeleton,
                    s.frameX * s.width, s.frameY * s.height, s.width, s.height,
                    s.deathX, s.deathY, s.width, s.height);

                s.x = randint(-30, canvas.width + 30);
                s.y = randint(-30, canvas.height + 30);
                if ((s.x > 0 && s.x < canvas.width) && (s.y > 0 && s.y < canvas.height)){ // if on the screen
                    
                    // 1 = up. 2 = right. 3 = down. 4 = left.
                    let random_direction = randint(1,4); // used to pick random direction
                    if (random_direction === 1){
                        s.y = s.y - canvas.height;
                    }
                    if (random_direction === 2){
                        s.x = s.x + canvas.width;
                    }
                    if (random_direction === 3){
                        s.y = s.y + canvas.height;
                    }
                    if (random_direction === 4){
                        s.x = s.x - canvas.width;
                    }
                }
                player.score = player.score + 25;
            }
        }
    }

    // Confine player
    if (playerhitBox.x < 0){
            player.x = player.x - playerhitBox.x; //100% 
    } 
    if ((playerhitBox.x + playerhitBox.width) >= canvas.width){
            player.x = canvas.width - (player.width - playerhitBox.width) - 0.1;
    } 
    if (playerhitBox.y < 0){
            player.y = playerhitBox.y - playerhitBox.height;
    }
    if (playerhitBox.y + playerhitBox.height >= canvas.height){
            player.y = canvas.height - player.height;
    }

    // Stats
    stats(player.score, time_elapsed);

    // Difficulty - Gradually increases as draw() runs
    blobsLimit = blobsLimit + 0.001;

    // Difficulty - Start adding skeletons after a certain amount of slimes
    if (blobsLimit > 6){
        skeletonLimit = skeletonLimit + 0.001; // start spawning roughly 30 seconds in.
    }
    
    
}

function randint(min, max) {
    return Math.round(Math.random() * (max - min)) + min;
}
function activate(event) {
    let key = event.key;

    if (key == " "){
        spaceBar = true;
    } else if (key === "ArrowLeft") {
        arrowLeft = true;
    } else if (key == "ArrowUp"){
        arrowUp = true;
    } else if (key == "ArrowRight"){
        arrowRight = true;
    } else if (key == "ArrowDown"){
        arrowDown = true;
    }
}
function deactivate(event) {
    let key = event.key;

    if (key == " "){
        spaceBar = false;    
    } else if (key === "ArrowLeft") {
        arrowLeft = false;
    } else if (key == "ArrowUp"){
        arrowUp = false;
    } else if (key == "ArrowRight"){
        arrowRight = false;
    } else if (key == "ArrowDown"){
        arrowDown = false;
    }
}
function player_enemy_collides(playerhitBox, b){

    if (playerhitBox.x + playerhitBox.width < b.hitboxX ||
        b.hitboxX + b.hitboxWidth < playerhitBox.x ||
        playerhitBox.y > b.hitboxY + b.hitboxHeight ||
        b.hitboxY > playerhitBox.y + playerhitBox.height){
            return false;
    } else {
        return true;
    }
}
function player_skeleton_collides(playerhitBox, s){

    if (playerhitBox.x + playerhitBox.width < s.hitboxX ||
        s.hitboxX + s.hitboxWidth < playerhitBox.x ||
        playerhitBox.y > s.hitboxY + s.hitboxHeight ||
        s.hitboxY > playerhitBox.y + playerhitBox.height){
            return false;
    } else {
        return true;
    }
}
function player_item_collides(playerhitBox, i){

    if (playerhitBox.x + playerhitBox.width < i.x ||
        i.x + i.width < playerhitBox.x ||
        playerhitBox.y > i.y + i.height ||
        i.y > playerhitBox.y + playerhitBox.height){
            return false;
    } else {
        return true;
    }
}
function player_obstacle_collides(playerhitBox, t){

    if (playerhitBox.x + playerhitBox.width < t.hitboxX ||
        t.hitboxX + t.hitboxWidth < playerhitBox.x ||
        playerhitBox.y > t.hitboxY + t.hitboxHeight ||
        t.hitboxY > playerhitBox.y + playerhitBox.height){
            return false;
    } else {
        return true;
    }
}
function enemy_melee_collides(meleeBox, b){
    
    if (meleeBox.x + meleeBox.width < b.x ||
        b.x + b.size < meleeBox.x ||
        meleeBox.y > b.y + b.size ||
        b.y > meleeBox.y + meleeBox.height){
            return false;
    } else {
        return true;
    }
}
function skeleton_melee_collides(meleeBox, s){
    
    if (meleeBox.x + meleeBox.width < s.hitboxX ||
        s.hitboxX + s.hitboxWidth < meleeBox.x ||
        meleeBox.y > s.hitboxY + s.hitboxHeight ||
        s.hitboxY > meleeBox.y + meleeBox.height){
            return false;
    } else {
        return true;
    }
}
function stats(score, time_elapsed) {

    let score_element = document.querySelector("#score");
    score_element.innerHTML = score;
    let time_element = document.querySelector("#time");
    time_element.innerHTML = time_elapsed;
    return   
}
function stop(message, score, time_elapsed) {

    window.removeEventListener("keydown", activate, false);
    window.removeEventListener("keyup", deactivate, false);
    window.cancelAnimationFrame(request_id);

    // display the outcome
    let outcome_element = document.querySelector("#outcome");
    outcome_element.innerHTML = message;

    // display the score
    let score_element = document.querySelector("#score");
    score_element.innerHTML = score;
    
    // display play again link
    let play_again_element = document.querySelector("#playagain");
    play_again_element.href = "https://cs1.ucc.ie/~rm30/cgi-bin/ca2/run.py/survival";
    play_again_element.innerHTML = "Play again";

    // display home link
    let home_element = document.querySelector("#home");
    home_element.href = "https://cs1.ucc.ie/~rm30/cgi-bin/ca2/run.py/";
    home_element.innerHTML = "Home";

    // Take score and time. Then store it.
    let data = new FormData();
    data.append("score", player.score);
    data.append("time", time_elapsed);

    xhttp = new XMLHttpRequest();
    xhttp.addEventListener("readystatechange", handle_response, false);
    xhttp.open("POST", "https://cs1.ucc.ie/~rm30/cgi-bin/ca2/run.py/store_score", true);
    xhttp.send(data);
}
function load_images(callback) { // loads images faster

    let num_images = Object.keys(IMAGES).length;
    let loaded = function() {

        num_images = num_images -1;
        if (num_images === 0){
            callback();
        }
    };
    for (let name of Object.keys(IMAGES)){
        let img = new Image();
        img.addEventListener("load", loaded, false);
        img.src = IMAGES[name];
        IMAGES[name] = img;
    }
}
function handle_response(){
    // Check that the response has fully arrived
    if( xhttp.readyState === 4 ){
        //Check the request was successful
        if ( xhttp.status === 200 ){
            if ( xhttp.responseText === "success" ){
                //score was successfully stored in database
                return "success"
            } else{
                //score was not successfully stored in database
                return "failure"
            }
        }
    }
}
