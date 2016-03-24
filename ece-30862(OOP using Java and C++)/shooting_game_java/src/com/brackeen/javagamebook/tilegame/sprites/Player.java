package com.brackeen.javagamebook.tilegame.sprites;

import com.brackeen.javagamebook.graphics.Animation;

/**
    The Player.
*/
public class Player extends Creature {

    private static final float JUMP_SPEED = -.95f;
    public int Health;
    public boolean shooting;
    public boolean Restmode = false;


    private boolean onGround;

    public Player(Animation left, Animation right,
        Animation deadLeft, Animation deadRight)
    {
        super(left, right, deadLeft, deadRight);
        this.Health = 20;
        
    }


    public void collideHorizontal() {
        setVelocityX(0);
    }


    public void collideVertical() {
        // check if collided with ground
        if (getVelocityY() > 0) {
            onGround = true;
        }
        setVelocityY(0);
    }


    public void setY(float y) {
        // check if falling
        if (Math.round(y) > Math.round(getY())) {
            onGround = false;
        }
        super.setY(y);
    }


    public void wakeUp() {
        // do nothing
    }


    /**
        Makes the player jump if the player is on the ground or
        if forceJump is true.
    */
    public void jump(boolean forceJump) {
        if (onGround || forceJump) {
            onGround = false;
            setVelocityY(JUMP_SPEED);
        }
    }
    
//    public void Down(boolean forceDown) {
//        if (onGround || forceDown) {
//            onGround = false;
//            setVelocityY(-1*JUMP_SPEED);
//        }
//    }
    


    public float getMaxSpeed() {
        return 0.5f;
    }
    
    public void setHealth(int dHealth) {
        // set new health equal to oldHealth+dHealth
        Health += dHealth;
        if (Health > 40) {
        	Health = 40;
        }
    }
    
    public void isShooting() {
        this.shooting = true;
    }
    
    public void isNotShooting() {
        this.shooting = false;
    }


	public void Down(boolean forceDown) {
		 if (!onGround || forceDown) {
	            onGround = true;
	            setVelocityY(-1*JUMP_SPEED);
	        }
	}
	
	public void setRestMode() {
		 Restmode = true;
	}

	public void waitasec() {
		 for(int i=0;i<1000000;i++)
		 {
			 for(int j =0;j<1000;j++)
			 {
				 
			 }
		 }
	}
	
}

