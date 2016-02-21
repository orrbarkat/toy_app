class AddDefaultToLevel < ActiveRecord::Migration
  def change
  	def up
  		change_column_default :users, :level, :integer,  0
	end

	def down
  		change_column_default :users, :level, :integer, nil
	end
  end
end
