package com.brackeen.javagamebook.tilegame;
import java.util.Date;
import java.util.LinkedList;

import java.awt.*;
import java.awt.event.KeyEvent;
import java.util.Iterator;

import javax.sound.midi.Sequence;
import javax.sound.midi.Sequencer;
import javax.sound.sampled.AudioFormat;

import com.brackeen.javagamebook.graphics.*;
import com.brackeen.javagamebook.sound.*;
import com.brackeen.javagamebook.input.*;
import com.brackeen.javagamebook.test.GameCore;
import com.brackeen.javagamebook.tilegame.sprites.*;

/**
    GameManager manages all parts of the game.
*/
public class GameManager extends GameCore {

    public static void main(String[] args) {
        new GameManager().run();
    }
    
    

    // uncompressed, 44100Hz, 16-bit, mono, signed, little-endian
    private static final AudioFormat PLAYBACK_FORMAT =
        new AudioFormat(44100, 16, 1, true, false);

    private static final int DRUM_TRACK = 1;

    public static final float GRAVITY = 0.002f;

	private static final String Rectangle = null;

    private Point pointCache = new Point();
    private TileMap map;
    private MidiPlayer midiPlayer;
    private SoundManager soundManager;
    private ResourceManager resourceManager;
    private Sound prizeSound;
    private Sound boopSound;
    private Sound CreatureHit;
    private Sound CreatureDied;
    private Sound ShotFired;
    private InputManager inputManager;
    private TileMapRenderer renderer;

    private GameAction moveLeft;
    private GameAction moveRight;
    private GameAction jump;
    private GameAction down; 
    private GameAction exit;
    private GameAction shoot;

    private static long Time = System.currentTimeMillis();
    private static long Time2 = System.currentTimeMillis();
    private static long BulletTime = System.currentTimeMillis(); // TODO
    
    private static int bulletCount = 0;
    private static int bulletCount2 = 0;
    private static int star_flag = 0;
    private static int cnt_bullets = 0;


    //private LinkedList<Bullet> b = new LinkedList<Bullet>();


    


    public void init() {
        super.init();

        // set up input manager
        initInput();

        // start resource manager
        resourceManager = new ResourceManager(
        screen.getFullScreenWindow().getGraphicsConfiguration());

        // load resources
        renderer = new TileMapRenderer();
        renderer.setBackground(
            resourceManager.loadImage("background.png"));

        // load first map
        map = resourceManager.loadNextMap();

        // load sounds
      soundManager = new SoundManager(PLAYBACK_FORMAT);
        prizeSound = soundManager.getSound("sounds/prize.wav");
        boopSound = soundManager.getSound("sounds/boop2.wav");
        CreatureHit = soundManager.getSound("sounds/CreatureHit.wav");
        CreatureDied = soundManager.getSound("sounds/CreatureDied.wav");
        ShotFired = soundManager.getSound("sounds/ShotFired.wav");

        // start music
        midiPlayer = new MidiPlayer();
        Sequence sequence =
            midiPlayer.getSequence("sounds/music.midi");
        midiPlayer.play(sequence, true);
        toggleDrumPlayback();
    }


    /**
        Closes any resurces used by the GameManager.
    */
    public void stop() {
        super.stop();
        midiPlayer.close();
        soundManager.close();
    }


    private void initInput() {
        moveLeft = new GameAction("moveLeft");
        moveRight = new GameAction("moveRight");
        jump = new GameAction("jump",
            GameAction.DETECT_INITAL_PRESS_ONLY);
        exit = new GameAction("exit",
            GameAction.DETECT_INITAL_PRESS_ONLY);
        shoot = new GameAction("shoot",
        		GameAction.DETECT_INITAL_PRESS_ONLY);
        down =  new GameAction("down",
                GameAction.DETECT_INITAL_PRESS_ONLY);

        inputManager = new InputManager(
            screen.getFullScreenWindow());
        inputManager.setCursor(InputManager.INVISIBLE_CURSOR);

        inputManager.mapToKey(moveLeft, KeyEvent.VK_LEFT);
        inputManager.mapToKey(moveRight, KeyEvent.VK_RIGHT);
        inputManager.mapToKey(jump, KeyEvent.VK_UP);
        inputManager.mapToKey(shoot, KeyEvent.VK_S);
        inputManager.mapToKey(exit, KeyEvent.VK_ESCAPE);
        inputManager.mapToKey(down, KeyEvent.VK_DOWN);

    }


   private void checkInput(long elapsedTime) {
    	
        if (exit.isPressed()) {
            stop();
        }
        float bulletvelocityX = 0;
        long currTime = System.currentTimeMillis();
        long currTime2 = System.currentTimeMillis();
        long currBulletTime = System.currentTimeMillis();
        boolean right,left,jumpu;
        boolean noShoot = false;
        
        right = left = jumpu = false;
        
        Player player = (Player)map.getPlayer();
        //Bullet[] bullets = new Bullet[10];
        //Bullet bullet = (Bullet)map.getBullet();
//        LinkedList<Bullet> b = new LinkedList<Bullet>;
        
        //player.isNotShooting();
        
        if (player.isAlive()) {
            float velocityX = 0;
 
            if (moveLeft.isPressed()) {
                velocityX-=player.getMaxSpeed();
                //System.out.println("MovingLeft");
                
                player.setHealth(1);
               
                left = true;
            }
            
            if (moveRight.isPressed()) {
                velocityX+=player.getMaxSpeed();
                //System.out.println("MovingRight");
                
                player.setHealth(1);
                    
                right = true;
            }
            
            if (jump.isPressed()) {
                player.jump(false);
                //System.out.println("Jumping");
                jumpu = true;
            }
  
            if (down.isPressed()) {
                player.Down(false);
                //System.out.println("Down");
            }
            
            
           /*if (!left && !right && !jumpu && (currTime - Time > 1000) ){
          	
                player.setHealth(5);
                    
            	Time = System.currentTimeMillis();
            }*/
            
            player.setVelocityX(velocityX);
            
            if (player.isAlive() && (currTime2 - Time2 > 900)) 
            {
            		grubshoot();
                //System.out.println("Down");
            }
            
           
            if(shoot.isPressed() && (currTime - Time > 3000)) {
            	
            	shoot.release();
            	player.Restmode = false;
        		//soundManager.play(ShotFired);
            	Bullet currBullet;
            	player.waitasec();
            	currBullet = (Bullet) map.getBullet();
            	currBullet.isAlivebu();
            	System.out.println("in shoot.isPressed: " + currBullet);
            	resourceManager.addSprite(map,currBullet,(int)player.getX(),(int)player.getY());
            	
            	//currBullet.isAlivebu();
            	if(player.getVelocityX() < 0)
            	{
            		currBullet.setX(player.getX()-50);	
            	}
            	else
            	{
            		currBullet.setX(player.getX()+80);
            	}
            	currBullet.setY(player.getY()+40);
            	System.out.println("Shooting..");
            	
            	if (Math.signum(player.getVelocityX()) >= 0) {
                	bulletvelocityX += currBullet.getMaxSpeed();	
            	}
            	else if (Math.signum(player.getVelocityX()) < 0) {
                	bulletvelocityX -= currBullet.getMaxSpeed() ;	
            	}
            	
            	currBullet.setVelocityX(bulletvelocityX);
            	
            	/*if(currBulletTime - BulletTime > 100) {
            		bulletCount++;
            		BulletTime = System.currentTimeMillis();
            		
            	}*/
            	
        		bulletCount++;

            	
            	if (bulletCount > 10) {
            		player.setRestMode();
            		bulletCount = 0;
                	Time = System.currentTimeMillis();
            	}
            }
        }
                       
   }
 
   public void draw(Graphics2D g) {
       renderer.draw(g, map,
           screen.getWidth(), screen.getHeight());
   }
       
   
   //makes the grub shoot
public void grubshoot(){

    float bulletvelocityX = 0;    
    Player player = (Player)map.getPlayer();
    
	   Iterator iter = map.getSprites();
	    
	   while (iter.hasNext()) {
	        Sprite grub = (Sprite)iter.next();
	        if(grub instanceof Grub)
	        {
		        Grub g = (Grub)grub;
	        	if(Math.abs(grub.getX() - player.getX()) <= 400)
	        	{
       		System.out.println("In grubshoot...");
       		if(Math.abs(grub.getX() - player.getX()) <= 300)
	        	{
           		Bullet currBullet;
               	currBullet = (Bullet) map.getBullet();
               	currBullet.isAlivebu();
               	System.out.println("in shoot.isPressed: " + currBullet);
               	resourceManager.addSprite(map,currBullet,(int)grub.getX(),(int)grub.getY());
               	
               	//currBullet.isAlivebu();
               	if(grub.getVelocityX() > 0)
               	{
               	currBullet.setX(grub.getX() + 50);
               	}
               	else{
	                	currBullet.setX(grub.getX());
               	}
               	currBullet.setY(grub.getY()+20);
               	System.out.println("Shooting..");
               	
               	if (Math.signum(grub.getVelocityX()) >= 0) {
                   	bulletvelocityX += currBullet.getMaxSpeed();	
               	}
               	else if (Math.signum(grub.getVelocityX()) < 0) {
                   	bulletvelocityX -= currBullet.getMaxSpeed() ;	
               	}
               	
               	currBullet.setVelocityX(bulletvelocityX);
	        	}
	        	}
	        	
	     	   bulletCount2++;

	     	   if (bulletCount2 > 1) 
	     	   {
	     		g.setRestMode();
	     	   	bulletCount2 = 0;
	     	    Time2 = System.currentTimeMillis();
	     	   }
	     	  if(Math.abs(grub.getX() - player.getX()) < 300)
	     	  {
	        	break;
	     	  }
	        }
	    }
}
    

    /**
        Gets the current map.
    */
    public TileMap getMap() {
        return map;
    }


    /**
        Turns on/off drum playback in the midi music (track 1).
    */
    public void toggleDrumPlayback() {
        Sequencer sequencer = midiPlayer.getSequencer();
        if (sequencer != null) {
            sequencer.setTrackMute(DRUM_TRACK,
                !sequencer.getTrackMute(DRUM_TRACK));
        }
    }


    /**
        Gets the tile that a Sprites collides with. Only the
        Sprite's X or Y should be changed, not both. Returns null
        if no collision is detected.
    */
    public Point getTileCollision(Sprite sprite,
        float newX, float newY)
    {
        float fromX = Math.min(sprite.getX(), newX);
        float fromY = Math.min(sprite.getY(), newY);
        float toX = Math.max(sprite.getX(), newX);
        float toY = Math.max(sprite.getY(), newY);

        // get the tile locations
        int fromTileX = TileMapRenderer.pixelsToTiles(fromX);
        int fromTileY = TileMapRenderer.pixelsToTiles(fromY);
        int toTileX = TileMapRenderer.pixelsToTiles(
            toX + sprite.getWidth() - 1);
        int toTileY = TileMapRenderer.pixelsToTiles(
            toY + sprite.getHeight() - 1);

        // check each tile for a collision
        for (int x=fromTileX; x<=toTileX; x++) {
            for (int y=fromTileY; y<=toTileY; y++) {
                if (x < 0 || x >= map.getWidth() ||
                    map.getTile(x, y) != null)
                {
                    // collision found, return the tile
                    pointCache.setLocation(x, y);
                    return pointCache;
                }
            }
        }

        // no collision found
        return null;
    }


    /**
        Checks if two Sprites collide with one another. Returns
        false if the two Sprites are the same. Returns false if
        one of the Sprites is a Creature that is not alive.
    */
    public boolean isCollision(Sprite s1, Sprite s2) {
        // if the Sprites are the same, return false
        if (s1 == s2) {
            return false;
        }

        // if one of the Sprites is a dead Creature, return false
        if (s1 instanceof Creature && !((Creature)s1).isAlive()) {
            return false;
        }
        if (s2 instanceof Creature && !((Creature)s2).isAlive()) {
            return false;
        }
        /*boolean check = s2 instanceof Creature && !(s2 instanceof Player);
        if (s1 instanceof Bullet && check) {
            return true;
        }*/

        // get the pixel location of the Sprites
        int s1x = Math.round(s1.getX());
        int s1y = Math.round(s1.getY());
        int s2x = Math.round(s2.getX());
        int s2y = Math.round(s2.getY());

        // check if the two sprites' boundaries intersect
        return (s1x < s2x + s2.getWidth() &&
            s2x < s1x + s1.getWidth() &&
            s1y < s2y + s2.getHeight() &&
            s2y < s1y + s1.getHeight());
    }


    /**
        Gets the Sprite that collides with the specified Sprite,
        or null if no Sprite collides with the specified Sprite.
    */
    public Sprite getSpriteCollision(Sprite sprite) {

        // run through the list of Sprites
        Iterator i = map.getSprites();
        while (i.hasNext()) {
            Sprite otherSprite = (Sprite)i.next();
            if (isCollision(sprite, otherSprite)) {
                // collision found, return the Sprite
                return otherSprite;
            }
        }

        // no collision found
        return null;
    }    

    /**
        Updates Animation, position, and velocity of all Sprites
        in the current map.
    */
    public void update(long elapsedTime) {
        Creature player = (Creature)map.getPlayer();
        //Creature bullet = (Creature)map.getBullet();

        

        // player is dead! start map over
        if (player.getState() == Creature.STATE_DEAD) {
            map = resourceManager.reloadMap();
            return;
        }

        // get keyboard/mouse input
        checkInput(elapsedTime);

        // update player
        updateCreature(player, elapsedTime);
        player.update(elapsedTime);
        
        //update bullet
        Iterator i2 = map.getBullets();
        while (i2.hasNext()) {
        	Bullet bullet = (Bullet)i2.next();
        	if (bullet.life) {
        	updateCreature(bullet, elapsedTime);
        	//System.out.println("BULLET UPDATE" + bullet);
        	}
        	if (bullet.getState() == Creature.STATE_DEAD) {
        		i2.remove();
        		System.out.println("Removed dead bullet");
        	}
        	
        	bullet.update(elapsedTime);
        }

        
        // update other sprites
        Iterator i = map.getSprites();
        while (i.hasNext()) {
        	Sprite sprite = (Sprite)i.next();
        	if (!(sprite instanceof Bullet)) {
        		if (sprite instanceof Creature) {
        			Creature creature = (Creature)sprite;
        			if (creature.getState() == Creature.STATE_DEAD) {
        				i.remove();
        			}

        			else {
        				updateCreature(creature, elapsedTime);
        			}
        		}
        		// normal update
        		sprite.update(elapsedTime);
        	}
        }
    }


    /**
        Updates the creature, applying gravity for creatures that
        aren't flying, and checks collisions.
    */
    private void updateCreature(Creature creature, long elapsedTime)
    {
        // apply gravity
        if (!creature.isFlying()) {
            creature.setVelocityY(creature.getVelocityY() + GRAVITY * elapsedTime);
        }

        // change x
        float dx = creature.getVelocityX();
        float oldX = creature.getX();
        float newX = oldX + dx * elapsedTime;
        Point tile = getTileCollision(creature, newX, creature.getY());
        if (tile == null) {
            creature.setX(newX);
        }
        
        else {
            // line up with the tile boundary
            if (dx > 0) {
                creature.setX(TileMapRenderer.tilesToPixels(tile.x) - creature.getWidth());
            }
            else if (dx < 0) {
                creature.setX(TileMapRenderer.tilesToPixels(tile.x + 1));
            }
            creature.collideHorizontal();
            
            if ((creature instanceof Bullet)) {
            	// TODO
            	// Kill the bullet
            	System.out.println("Bullet hit X of tile");
                //checkBulletCollision((Bullet)creature, false);
            	creature.setState(Creature.STATE_DYING);
            }
        }
        if (creature instanceof Player) {
            checkPlayerCollision((Player)creature, false);
        }
        

        // change y
        float dy = creature.getVelocityY();
        float oldY = creature.getY();
        float newY = oldY + dy * elapsedTime;
        tile = getTileCollision(creature, creature.getX(), newY);
        if (tile == null) {
            creature.setY(newY);
        }
        else {
            // line up with the tile boundary
            if (dy > 0) {
                creature.setY(
                    TileMapRenderer.tilesToPixels(tile.y) - creature.getHeight());
            }
            else if (dy < 0) {
                creature.setY(
                    TileMapRenderer.tilesToPixels(tile.y + 1));
            }
            creature.collideVertical();
        }
        if (creature instanceof Player) {
            boolean canKill = (oldY < creature.getY());
            checkPlayerCollision((Player)creature, canKill);
        }
        
        if (creature instanceof Bullet) {
            boolean canKill = true;
			checkBulletCollision((Bullet)creature, canKill);

			}
        
    }

    

    /**
        Checks for Player collision with other Sprites. If
        canKill is true, collisions with Creatures will kill
        them.
    */
    public void checkPlayerCollision(Player player, boolean canKill)
        {
        Sprite collisionSprite = getSpriteCollision(player);
            if (!player.isAlive()) {
                return;
            }
            
            if (collisionSprite instanceof PowerUp) {
                acquirePowerUp((PowerUp)collisionSprite);
            }
            
            if(collisionSprite instanceof Creature)
            {
            	if (canKill)
            	{
            		 Creature badguy = (Creature)collisionSprite;
            		 player.setY(badguy.getY() - player.getHeight());
                     player.jump(true);
                     badguy.setState(1);
                     player.setHealth(10);
            	}
            	else
            	{
            		player.setState(1);
            	}
            }
       
        }
    
    
    /**
    Checks for Bullet collision with other Sprites. If
    canKill is true, collisions with Creatures will kill
    them.
*/
public void checkBulletCollision(Bullet bullet, boolean canKill)
    {
		Sprite Hero = map.getPlayer();
		if(isCollision(bullet, Hero))
		{
			Player p = (Player)Hero;
			if(star_flag == 0)
			{
			p.setHealth(-5);
			}
			cnt_bullets++;
			if(cnt_bullets == 3)
			{
				star_flag = 0;
				cnt_bullets = 0;
			}
			if(p.Health == 0)
			{
				p.setState(1);
			}
			bullet.setState(2);
		}
        // check for Bullet collision with other sprites
        Sprite collisionSprite = getSpriteCollision(bullet);
        
       if((collisionSprite instanceof Creature) && !(collisionSprite instanceof Player) && !(collisionSprite instanceof Bullet))
       {
    	   if (canKill)
       	   {
       		 Creature badguy = (Creature)collisionSprite;
             badguy.setState(2);
             bullet.setState(2);
             ((Player) Hero).setHealth(10);       	   
           }

        }
    }



    /**
        Gives the player the speicifed power up and removes it
        from the map.
    */
    public void acquirePowerUp(PowerUp powerUp) {
        // remove it from the map
        map.removeSprite(powerUp);
        Sprite player = map.getPlayer();
        Player player2 = (Player) player;
        if (powerUp instanceof PowerUp.Mush) {
            // do something here, like give the player points
        	player2.setHealth(5);
            //soundManager.play(prizeSound);
        }
        else if (powerUp instanceof PowerUp.gas ) {
        	
        	player2.setRestMode();
            Time = System.currentTimeMillis();
            /// wait 10 seconds
            player2.Restmode = false;
        }
        else if(powerUp instanceof PowerUp.explod){
        	player2.setHealth(-10);
            //soundManager.play(prizeSound);
        }
        else if (powerUp instanceof PowerUp.Music) {
            // change the music
            //soundManager.play(prizeSound);
            toggleDrumPlayback();
        }
        else if (powerUp instanceof PowerUp.Star) {
        	star_flag = 1;
        }
        else if (powerUp instanceof PowerUp.Goal) {
            // advance to next map
            //soundManager.play(prizeSound,new EchoFilter(2000, .7f), false);
            map = resourceManager.loadNextMap();
        }
    }

}
