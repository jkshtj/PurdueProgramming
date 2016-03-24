package com.brackeen.javagamebook.tilegame.sprites;

import com.brackeen.javagamebook.graphics.Animation;
/**
    The Bullet.
*/
public class Bullet extends Creature  {

    public boolean life;
    
    
    
//    public Bullet (double x){
//    	this.x = x;
//    }

    public Bullet(Animation left, Animation right,
        Animation deadLeft, Animation deadRight)
    {
        super(left, right, deadLeft, deadRight);
        this.life = false;
        
    }


    public void collideHorizontal() {
        setVelocityX(0);
    }

    public void wakeUp() {
        // do nothing
    }

    public float getMaxSpeed() {
        return 1f;
    }
    
	
	public void isAlivebu() {
		this.life = true;
		
	}
	
	public void isDead() {
		this.life = false;
	}
	
	 public boolean isFlying() {
	    return this.life;
	}

		
	}

