namespace :midbern do 
	desc "get a registration"
	task :sign_up do
		require 'rubygems'
		# require 'sinatra'
		require 'json'
		require 'open-uri'
		#require 'net/http'
		require 'net/https'
		# require 'rest-client'
		# require 'nokogiri'

		# set :environment, :production

		get '/' do

		  uri = ("https://teamtreehouse.com/community/open-https-webpage-in-ruby")


		  url2 = "http://slashdot.org/"


		    begin
		       redirect (uri)
		    rescue
		    doc = open(url2)

		    end
		end
	end
end